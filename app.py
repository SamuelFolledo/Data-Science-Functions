data = [1, 3, 5, 2, 3, 7, 8, 4, 10, 0, 6, 7, 3, 0, 3, 0, 5, 7, 10, 1, 4, 9, 3]

x_list = [3.3,4.4,5.5,6.71,6.93,4.168,9.779,6.182,7.59,2.167,7.042,10.791,5.313,7.997,5.654,9.27,3.1]


y_list = [1.7,2.76,2.09,3.19,1.694,1.573,3.366,2.596,2.53,1.221,2.827,3.465,1.65,2.904,2.42,2.94,1.3]

# print(f"Mean = {mean(data)}")

def mean(list): #gets a list and returns the average a.k.a. central tendency
    return(float(sum(list)) / len(list))

def sum(list):
    total = 0
    for i in list:
        total += i
    return total

def median(list):
    length = len(list)
    sortedData = sorted(list)
    print(f"Sorted Data = {sortedData}")
    if length < 1: #if length < 0, return None
        return None
    
    if length % 2 == 1: #length of list is odd
        return sortedData[length // 2]
        # return np.median(sortedData)
    else: #length of list is even, then get the average of the 2 middle
        firstElement = sortedData[length // 2]
        secondElement = sortedData[length // 2 - 1]
        print(firstElement)
        print(secondElement)
#         compute_mean([sortedData[firstElement], sortedData[secondElement]])
        median = (firstElement + secondElement) / 2
        return median

def percentile(data, percent):
    #first we want to sort the data in ascending order
    # data = np.sort(data)
    #then we will get the index
    
    index = (percent/100)* len(data)
    #we will have to round up to the nearest whole number using the ceiling method and covert to an int
    # index = int(np.ceil(index))
    
    return data[index-1] #adjust by -1 since indices start with 0

print(f"Sum = {sum(data)}")
print(f"Length = {len(data)}")
print(f"Mean = {mean(data)}")
print(f"Median = {median(data)}")
