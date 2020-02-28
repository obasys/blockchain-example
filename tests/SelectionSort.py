data = [3, 60, 35, 2, 45, 320, 5]

def selection_sort(data):

    for value in range(data, 0, -1):
        smallestValueIndex = value.index()
        print(smallestValueIndex)

        for location in range(1, value+1):
            if data[location] > data[smallestValueIndex]:
                smallestValueIndex = location

        temp = data[value.index()]
        data[value.index()] = data[smallestValueIndex]
        data[smallestValueIndex] = temp
        print(data[value.index()])

selection_sort(data)
