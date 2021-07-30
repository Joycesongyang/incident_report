import requests
import shutil
import re
from datetime import datetime
import os
import tabula
import pandas as pd
from collections import Counter
import tempfile
import argparse

def count_nature(url):
    match = re.search(r'\d{4}-\d{2}-\d{2}', url)
    date = datetime.strptime(match.group(), '%Y-%m-%d').date()
    #extract the date to be the file name
    file_name = str(date) + ".pdf"

    #create a new folder if it doesn't exist
    folder = tempfile.mkdtemp()

    r = requests.get(url, auth=('usrname', 'password'), verify=False,stream=True)
    r.raw.decode_content = True
    path = os.path.join("/{}/{}".format(folder, file_name))
    with open(path, 'wb') as f:
            shutil.copyfileobj(r.raw, f) 

    # extract the information from pdf into csv
    df_name = str(date) + ".csv"
    folder2 = tempfile.mkdtemp()
    out_path = os.path.join("/{}/{}".format(folder2, df_name))
    tabula.io.convert_into(path, out_path, output_format="csv", pages='all', stream = True)
    df = pd.read_csv(out_path,usecols = ['Nature'])

    #clean and sort the data
    df_new = df.dropna()
    nature_list = df_new['Nature'].tolist()
    nature_list.sort()
    result = Counter(nature_list)
    for key, value in result.items():
            print(key, ' | ', value)

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--incidents",
                        type=str,
                        required=True,
                        help="Incident summary url.")
    args = parser.parse_args()
    count_nature(args.incidents)