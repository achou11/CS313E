# File: sorting.py
# Description: Program compares efficiencies of different list sorting methods with different types of lists.
# Student's Name: Andrew Chou
# Student's UT EID: aoc349
# Course Name: CS 313E
# Unique Number: 51320

# Date Created: 11/18/16
# Date Last Modified: 11/18/16

#import necessary libraries
import random
import time
import sys
sys.setrecursionlimit(10000)


#different sorting methods and their helper methods
def bubbleSort(alist):
    for passnum in range(len(alist)-1,0,-1):
        for i in range(passnum):
            if alist[i] > alist[i+1]:
                temp = alist[i]
                alist[i] = alist[i+1]
                alist[i+1] = temp

def selectionSort(alist):
    for fillslot in range(len(alist)-1,0,-1):
        positionOfMax = 0
        for location in range(1,fillslot+1):
            if alist[location] > alist[positionOfMax]:
                positionOfMax = location
        temp = alist[fillslot]
        alist[fillslot] = alist[positionOfMax]
        alist[positionOfMax] = temp


def insertionSort(alist):
    for index in range(1,len(alist)):
        currentvalue = alist[index]
        position = index

        while position>0 and alist[position-1]>currentvalue:
            alist[position] = alist[position-1]
            position = position-1

        alist[position] = currentvalue

def shellSort(alist):
    sublistcount = len(alist)//2
    while sublistcount > 0:
        for startposition in range(sublistcount):
            gapInsertionSort(alist,startposition,sublistcount)
        sublistcount = sublistcount // 2

def gapInsertionSort(alist,start,gap):
    for i in range(start+gap,len(alist),gap):
        currentvalue = alist[i]
        position = i

        while position>=gap and alist[position-gap]>currentvalue:
            alist[position] = alist[position-gap]
            position = position - gap

        alist[position] = currentvalue

def mergeSort(alist):
    if len(alist) > 1:
        mid = len(alist) // 2
        lefthalf = alist[:mid]
        righthalf = alist[mid:]

        mergeSort(lefthalf)
        mergeSort(righthalf)

        i = 0
        j = 0
        k = 0

        while i<len(lefthalf) and j<len(righthalf):
            if lefthalf[i] < righthalf[j]:
                alist[k] = lefthalf[i]
                i += 1
            else:
                alist[k] = righthalf[j]
                j += 1
            k += 1

        while i < len(lefthalf):
            alist[k] = lefthalf[i]
            i += 1
            k += 1

        while j < len(righthalf):
            alist[k] = righthalf[j]
            j += 1
            k += 1

def quickSort(alist):
    quickSortHelper(alist,0,len(alist)-1)

def quickSortHelper(alist,first,last):
    if first < last:
        splitpoint = partition(alist,first,last)
        quickSortHelper(alist,first,splitpoint-1)
        quickSortHelper(alist,splitpoint+1,last)

def partition(alist,first,last):
    pivotvalue = alist[first]
    leftmark = first + 1
    rightmark = last
    done = False

    while not done:

        while leftmark <= rightmark and alist[leftmark] <= pivotvalue:
            leftmark += 1

        while alist[rightmark] >= pivotvalue and rightmark >= leftmark:
            rightmark -= 1

        if rightmark < leftmark:
            done = True
        else:
            temp = alist[leftmark]
            alist[leftmark] = alist[rightmark]
            alist[rightmark] = temp

    temp = alist[first]
    alist[first] = alist[rightmark]
    alist[rightmark] = temp

    return rightmark


def main():

    for listType in range(4):

        #random list
        if listType == 0:
            print()
            print ("Input Type = Random")
            print ("                    avg time   avg time   avg time")
            print ("   Sort function     (n=10)    (n=100)    (n=1000)")
            print ("-----------------------------------------------------")

        #sorted list
        if listType == 1:
            print()
            print ("Input Type = Sorted")
            print ("                    avg time   avg time   avg time")
            print ("   Sort function     (n=10)    (n=100)    (n=1000)")
            print ("-----------------------------------------------------")

        #reverse sorted list
        if listType == 2:
            print()
            print ("Input Type = Reverse")
            print ("                    avg time   avg time   avg time")
            print ("   Sort function     (n=10)    (n=100)    (n=1000)")
            print ("-----------------------------------------------------")

        #almost sorted list
        if listType == 3:
            print()
            print ("Input Type = Almost Sorted")
            print ("                    avg time   avg time   avg time")
            print ("   Sort function     (n=10)    (n=100)    (n=1000)")
            print ("-----------------------------------------------------")


        #perform time trials for n = 10, 100, 1000 for each sorting method 6 times (once for each method)
        for sort in range(6):

            # 10 items in list
            n = 10

            #randomly generated list
            if listType == 0:
                myList = [i for i in range(n)]
                random.shuffle(myList)

            #sorted list
            if listType == 1:
                myList = [i for i in range(n)]

            ##reverse sorted list
            if listType == 2:
                myList = [i for i in range(n)]
                myList.reverse()

            #almost sorted list
            if listType == 3:
                myList = [i for i in range(n)]
                for i in range(n//10):
                    randomIndex1 = random.randint(0,len(myList)-1)
                    randomIndex2 = random.randint(0,len(myList)-1)
                    temp = myList[randomIndex1]
                    temp2 = myList[randomIndex2]
                    myList[randomIndex1] = temp2
                    myList[randomIndex2] = temp


            sum10 = 0

            for i in range(5):
                if sort == 0:
                    sortType = "bubbleSort"
                    startTime = time.perf_counter()
                    bubbleSort(myList)
                    endTime = time.perf_counter()
                if sort == 1:
                    sortType = "selectionSort"
                    startTime = time.perf_counter()
                    selectionSort(myList)
                    endTime = time.perf_counter()
                if sort == 2:
                    sortType = 'insertionSort'
                    startTime = time.perf_counter()
                    insertionSort(myList)
                    endTime = time.perf_counter()
                if sort == 3:
                    sortType = "shellSort"
                    startTime = time.perf_counter()
                    shellSort(myList)
                    endTime = time.perf_counter()
                if sort == 4:
                    sortType = "mergeSort"
                    startTime = time.perf_counter()
                    mergeSort(myList)
                    endTime = time.perf_counter()
                if sort == 5:
                    sortType = "quickSort"
                    startTime = time.perf_counter()
                    quickSort(myList)
                    endTime = time.perf_counter()

                elapsedTime = endTime - startTime
                sum10 += elapsedTime


            avg10 = sum10 / 5

            #100 items in list
            n = 100

            #randomly generated list
            if listType == 0:
                myList = [i for i in range(n)]
                random.shuffle(myList)

            #sorted list
            if listType == 1:
                myList = [i for i in range(n)]

            #reverse sorted list
            if listType == 2:
                myList = [i for i in range(n)]
                myList.reverse()

            #almost sorted list
            if listType == 3:
                myList = [i for i in range(n)]
                for i in range(n//10):
                    randomIndex1 = random.randint(0,len(myList)-1)
                    randomIndex2 = random.randint(0,len(myList)-1)
                    temp = myList[randomIndex1]
                    temp2 = myList[randomIndex2]
                    myList[randomIndex1] = temp2
                    myList[randomIndex2] = temp

            sum100 = 0

            for i in range(5):
                if sort == 0:
                    startTime = time.perf_counter()
                    bubbleSort(myList)
                    endTime = time.perf_counter()
                if sort == 1:
                    startTime = time.perf_counter()
                    selectionSort(myList)
                    endTime = time.perf_counter()
                if sort == 2:
                    startTime = time.perf_counter()
                    insertionSort(myList)
                    endTime = time.perf_counter()
                if sort == 3:
                    startTime = time.perf_counter()
                    shellSort(myList)
                    endTime = time.perf_counter()
                if sort == 4:
                    startTime = time.perf_counter()
                    mergeSort(myList)
                    endTime = time.perf_counter()
                if sort == 5:
                    startTime = time.perf_counter()
                    quickSort(myList)
                    endTime = time.perf_counter()

                elapsedTime = endTime - startTime
                sum100 += elapsedTime

            avg100 = sum100 / 5

            # 1000 items in list
            n = 1000

            #random list
            if listType == 0:
                myList = [i for i in range(n)]
                random.shuffle(myList)

            #sorted list
            if listType == 1:
                myList = [i for i in range(n)]

            #reverse sorted list
            if listType == 2:
                myList = [i for i in range(n)]
                myList.reverse()

            #almost sorted list
            if listType == 3:
                myList = [i for i in range(n)]
                for i in range(n//10):
                    randomIndex1 = random.randint(0,len(myList)-1)
                    randomIndex2 = random.randint(0,len(myList)-1)
                    temp = myList[randomIndex1]
                    temp2 = myList[randomIndex2]
                    myList[randomIndex1] = temp2
                    myList[randomIndex2] = temp


            sum1000 = 0

            for i in range(5):
                if sort == 0:
                    startTime = time.perf_counter()
                    bubbleSort(myList)
                    endTime = time.perf_counter()
                if sort == 1:
                    startTime = time.perf_counter()
                    selectionSort(myList)
                    endTime = time.perf_counter()
                if sort == 2:
                    startTime = time.perf_counter()
                    insertionSort(myList)
                    endTime = time.perf_counter()
                if sort == 3:
                    startTime = time.perf_counter()
                    shellSort(myList)
                    endTime = time.perf_counter()
                if sort == 4:
                    startTime = time.perf_counter()
                    mergeSort(myList)
                    endTime = time.perf_counter()
                if sort == 5:
                    startTime = time.perf_counter()
                    quickSort(myList)
                    endTime = time.perf_counter()

                elapsedTime = endTime - startTime
                sum1000 += elapsedTime

            avg1000 = sum1000 / 5

            print (sortType.rjust(17, " "), format(avg10, '.6f').rjust(10, " "), format(avg100, '.6f').rjust(10, " "), format(avg1000, '.6f').rjust(10, " "))

        print ()


main()
