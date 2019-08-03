#import modules
import pandas as pd
import csv
import os
import numpy as np

#helper function to amalgimate csv files
def csv_amalgimation(filename):
    csv_df = pd.read_csv(filename, encoding="latin1", parse_dates=[5])
    columns = ['Position', 'Track Name', 'Artist', 'Streams', 'URL', 'Date']
    csv_df.columns = columns
    return csv_df

#defining location of files to amalgimate
csv_path = os.getcwd() + '\\Top_200_Spotify_Data\\'

#creating list of csv files to combine 
csv_list = []
for subdir, dirs, files in os.walk(csv_path):
    for file in files:
        csv_list.append(os.path.join(subdir, file))

#creating lists to house dataframes to append and list of the names of csv files where errors occured
dfs_to_append = []
error_csvs = []
for csv_ in csv_list:
    try:
        dfs_to_append.append(csv_amalgimation(csv_))
    except:
        error_csvs.append(csv_)
        pass

#appending csv files
df = pd.DataFrame()
df = df.append(dfs_to_append, ignore_index=True)

#writing appended csv files to an amalgimated csv for analysis
#C:\Users\abels\Desktop\spotify_scrape\Data\csv_files\
write_path = os.getcwd() + '\\final_csv_files\\'

#formatting/removing headers from all csv files
df['Streams'] = pd.to_numeric(df['Streams'], errors='coerce')
mask = (~np.isnan(df['Streams']))
df = df[mask]
df.to_csv(write_path + 'Combined_Top_200_Stream_Numbers.csv')

#writing files that errored to csv for review
with open(write_path + 'error_files.csv', 'w', newline='') as myfile:
    wr = csv.writer(myfile, delimiter=',')
    for line in error_csvs:
        wr.writerow([line])