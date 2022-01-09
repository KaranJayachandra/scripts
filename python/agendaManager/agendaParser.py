from pandas import DataFrame
from datetime import datetime

def readData(fileName):
    with open(fileName, 'r') as filePointer:
        lines = filePointer.readlines()
        filePointer.flush()
        filePointer.close()
    return lines

def parseFinanceData(lines):
    financeData = []
    for line in lines:
        if line.__contains__('###'):
            line = line.replace('#', '')
            line = line.replace('\n', '')
            currentDate = datetime.strptime(line.replace(' ', ''), "%Y-%m-%d")
        if (line.__contains__('EUR') and line.__contains__(':')):
            # Cleaning up the line and splitting into fields 
            line = line.replace('- ', '')
            properties = line.split(':')
            
            # Selecting the data
            itemName = properties[0]
            itemCost = properties[1]
            itemCategory = properties[2]

            # Cleaning up the data for storing
            if itemName[-1] == ' ':
                itemName = itemName[:-1]
            itemCost = itemCost.replace('EUR', '')
            itemCost = float(itemCost.replace(' ', ''))
            itemCategory = itemCategory.replace(' ', '')
            itemCategory = itemCategory.replace('\n', '')

            financeData.append([currentDate, itemName, itemCost, itemCategory])
    financeData = DataFrame(financeData, columns=['Date', 'Item', 'Cost', 'Category']) 
    return financeData

def spendByCategory(financeData):
    return financeData.groupby(['Category'])['Cost'].sum()

data = parseFinanceData(readData('test1.md'))
print(data)
data = spendByCategory(data)
print(data)
