
#Author: Adam Kent
import csv
import random
import datetime
import numpy as np

def script(filenum, percentpos):
    
    #convert file suffix to 3 digit string
    filenum1 = str(filenum)
    if len(filenum1) == 1:
        filenum1 = str("0" + filenum1)
    percentpos1 = str(percentpos)
    if len(percentpos1) == 1:
        percentpos1 = str("00" + percentpos1)
    elif len(percentpos1) == 2:
        percentpos1 = str("0"+percentpos1)

    #create ELUTE column values
    fullplatecode = ("ELUTE" + percentpos1 + "99999")
    #initialise csv clumns
    fieldnames=['Root Sample ID','Plate','Well','Result','Date Tested', 'Lab ID', 'testKit','CH1-Target','CH1-Result','CH1-Cq','CH2-Target','CH2-Result','CH2-Cq','CH3-Target','CH3-Result','CH3-Cq','CH4-Target','CH4-Result','CH4-Cq']
    
    writer = csv.DictWriter(open(fullplatecode + str(filenum1) + ".csv", "w", newline =''), fieldnames=fieldnames)

    #create and shuffle list of 93 boolean values at proportion of percentpos
    results = []
    x = (0.93 * percentpos)
    y = (0.93 * (100-percentpos))
    xx = int(round(x))
    yy = int(round(y))
  
    for i in range(xx):
        results.append(1)
    for i in range(yy):
        results.append(0)
    if len(results) == 92:
        either = [0,1]
        results.append(random.choice(either))
    random.shuffle(results)
    print("Creating " + str(len(results)) + " results")

    #create and shuffle list containing 93 wells without 3 control wells
    wellslayout = ['A01', 'A02', 'A03', 'A04', 'A05', 'A06', 'A07', 'A08', 'A09' ,'A10', 'A11', 'A12',
            'B01', 'B02', 'B03', 'B04', 'B05', 'B06', 'B07', 'B08', 'B09' ,'B10', 'B11', 'B12',
            'C01', 'C02', 'C03', 'C04', 'C05', 'C06', 'C07', 'C08', 'C09' ,'C10', 'C11', 'C12',
            'D01', 'D02', 'D03', 'D04', 'D05', 'D06', 'D07', 'D08', 'D09' ,'D10', 'D11', 'D12',
            'E01', 'E02', 'E03', 'E04', 'E05', 'E06', 'E07', 'E08', 'E09' ,'E10', 'E11', 'E12',
            'F01', 'F02', 'F03', 'F04', 'F05', 'F06', 'F07', 'F08', 'F09' ,'F10', 'F11', 'F12',
            'G01', 'G02', 'G03', 'G04', 'G05', 'G06', 'G07', 'G08', 'G09' ,'G10', 'G11', 'G12',
            'H01', 'H02', 'H03', 'H04', 'H05', 'H06', 'H07', 'H08', 'H09']
    random.shuffle(wellslayout)
    #write csv files
    writer.writerow(dict(zip(fieldnames, fieldnames)))
    for i in range(0, 93):
        well = wellslayout.pop()
        rsi = ("VVV" + str(random.randint(10000000, 99999999)) + "_" + fullplatecode + "_" + well)
        result = results.pop()
        print(results)
        date = datetime.datetime.today().strftime('%d/%m/%Y %H:%M:%S UTC')
        if result == 1:
            resultstr = str("Positive")
        else:
            continue
        writer.writerow(dict([
        ('Root Sample ID', rsi ),
        ('Plate', fullplatecode),
        ('Well', well),
        ('Result', resultstr ),
        ('Date Tested', date),
        ('Lab ID', 'LML'),
        ('testKit', 'ePCR'),
        ('CH1-Target', 'Unknown'),
        ('CH1-Result', 'Unknown'),
        ('CH1-Cq', 'Unknown'),
        ('CH2-Target', 'Unknown'),
        ('CH2-Result', 'Unknown'),
        ('CH2-Cq', 'Unknown'),
        ('CH3-Target', 'Unknown'),
        ('CH3-Result', 'Unknown'),
        ('CH3-Cq', 'Unknown'),
        ('CH4-Target', 'Unknown'),
        ('CH4-Result', 'Unknown'),
        ('CH4-Cq', 'Unknown')]))

def main():
    #list desired percentage values to test then enumerate through list via for loop
    percentages = [2,5,10,20,50,100]
    for percent in percentages:
        percentpos = percent
        #enumerate through numbers 1 to 12 for filename suffixes
        for x in range (1,13):
            script(x, percentpos)


if __name__ == "__main__":
    main()