numberList = [1,23,4,5,7,39,22,33,60,207,1024,6,9,4096]
largestNumber = numberList[0]
for item in numberList:
    if item > largestNumber:
        largestNumber = item
print(f"The largest number is: {largestNumber}!")
