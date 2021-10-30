list = [2,1,100,343,32,34,234,2,31,6,547,567,43,53,2,4,2]

def binary_search(data, value):
    low = 0
    high = len(data) - 1
    while (low <= high):
        mid = (low+high)/2
        if (data[mid] == value):
            return mid
        elif(data[mid] < value):
            low = mid+1
        else:
            high = mid-1
    return -1

def bubble_sort(data):
    n = len(data)
    for i in range(n-1):
        for j in range(0,n-i-1):
            if data[j] > data[j +1]:
                data[j], data[j+1] = data[j+1], data[j]


def merge_sort(data):
    if len(data) > 1:
        mid = len(data)//2
        L = data[:mid]
        R = data[mid:]

        merge_sort(L)
        merge_sort(R)

        i = j= k =0

        while i < len(L):
            data[k] = R[j]
            i+=1
            k+=1
        while i < len(R):
            data[k] = R[j]
            j+=1
            k+=1


def quick_sort(sequence):
    length = len(sequence)
    if length <= 1:
        return sequence
    else:
        pivot = sequence.pop()

    items_greater = []
    items_lower = []

    for item in sequence:
        if item >= pivot:
            items_greater.append(item)

        else:
            items_lower.append(item)

    return quick_sort(items_lower) + [pivot] + quick_sort(items_greater)
