from os import walk

def main():
    print("Enter location of test vector:")
    list = walk(input())
    csvOutput = 'Test Vector, Test Name, Sub Test Name, Number of Vectors\n'
    for item in list:
        folderPath = item[0]
        if 'adc_samples' in folderPath:
            pathList = folderPath.split('\\')
            testVector = pathList[1]
            testName = pathList[2]
            subTestName = pathList[3]
            nFiles = len(item[2])
            lineOutput = f"{testVector}, {testName}, {subTestName}, {nFiles}"
            csvOutput += lineOutput + '\n'
            print(lineOutput)
    with open('output.csv', 'w') as csvFile:
        csvFile.write(csvOutput)

if __name__ == '__main__':
    main()