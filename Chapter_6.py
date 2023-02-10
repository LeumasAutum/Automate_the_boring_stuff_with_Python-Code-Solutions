def printTable(tableData):
    # Find the longest string in each list of the table
    colWidths = [0] * len(tableData)
    for i in range(len(tableData)):
        max_len = 0
        for item in tableData[i]:
            if len(item) > max_len:
                max_len = len(item)
        colWidths[i] = max_len

    # Print the table
    for i in range(len(tableData[0])):
        for j in range(len(tableData)):
            print(tableData[j][i].rjust(colWidths[j]), end=' ')
        print()

tableData = [['apples', 'oranges', 'cherries', 'banana'], 
 ['Alice', 'Bob', 'Carol', 'David'], 
 ['dogs', 'cats', 'moose', 'goose']]
printTable(tableData)
