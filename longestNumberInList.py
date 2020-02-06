#Largest Number
numberList = [1,23,4,5,7,39,22,33,60,4,207,1024,6,9,9,9,7,7,7]
numberList.sort()
print(f"The largest number is: {numberList[-1]}!")

#Remove Duplicates
print(numberList)
uniques = []
for number in numberList:
    if number not in uniques:
        uniques.append(number)
print(uniques)