
import pandas as pd 
from pandas import DataFrame 
import csv


def prepared_csv(location, location2):
    # read through a csv, change the row you need to then save it to a new file

    with open(location, 'r') as f:
        csv_reader = csv.reader(f, delimiter=',')
        title = next(csv_reader)
        lines = []        
        
        for line in csv_reader:    # line is a row in the csv file
            lines.append(line)

    csv_df = pd.DataFrame(columns = title, data = lines, index=None)
    
    # save changes to new csv file 
    with open(location2, 'w', newline='') as f:
        writer = csv.writer(f, delimiter=',')
        writer.writerow(title) #write the first row to be the header row
        writer.writerows(lines)#write the rest of the tuple to be the rest of csv file
    
    csv_data = pd.read_csv(location2)
    #print(csv_data)
    
    #returns dataframe
    return csv_data #returns dataframe