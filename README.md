# Incidents Report

## Target results
the format should be: 

Nature | (number of occurance)
with nature sorted by alphabetical order

**as follows**:

911 Call Nature Unknown  |  3 

Abdominal Pains/Problems  |  1 

Alarm  |  11 

Alarm Holdup/Panic  |  5 

Allergies/Envenomations  |  2 

Animal Complaint  |  3 

Animal Dead  |  2 

Animal Injured  |  1 

Animal Trapped  |  3 

Animal at Large  |  1 

Assault EMS Needed  |  4 

Assist Fire  |  1 

Breathing Problems  |  9 

Burglary  |  3 

COP Problem Solving  |  1 

COP Relationships  |  2 

Check Area  |  6 

Chest Pain  |  4 

Civil Standby  |  1 

Contact a Subject  |  10 

Diabetic Problems  |  2 

Disturbance/Domestic  |  23 

Drunk Driver  |  2 

## Source
the data is from the files on the public websites of local police department

## Run this program
python this_project.py --incidents https://www.normanok.gov/sites/default/files/documents/2021-07/2021-07-28_daily_incident_summary.pdf
* you can change the url by looking for different days on the website

## TIPS
* import basic libraries
* use Tabula to directly convert pdf file into dataframe.
The prerequisite of using tabula: install Java, tabula, python

## Function detail

* the only parameter is the url
* extract the date in the url to be the file name saved in temporary folder1
* fetch the raw data and convert it into dataframe
* read the dataframe, extract and clean the target column 'Nature'
* convert the column into sorted list, count and print the target result

## __Main__
* use Argparse to execute the function
* Argpase is a command-line parsing module in the Python standard library.


# Author and contact
joycesongyang@gmail.com