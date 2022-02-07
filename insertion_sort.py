

przyklad = [7,5,2,33,10,1,3,33,23,1,12,3,99,0]

# def insertion_sort(array):
#     temp = array[0]
#     for i in range(len(array)):
#         for y in range(i+1,len(array)):
#             if array[i] > array[y]:
#                 pass
#
#
#         print(i)
#
#
#     return array
#     # 2,5,7
#
# print(insertion_sort(przyklad))
def insertion_sort(array):

    # We start from 1 since the first element is trivially sorted
    for index in range(1, len(array)):
        currentValue = array[index]
        currentPosition = index

        # As long as we haven't reached the beginning and there is an element
        # in our sorted array larger than the one we're trying to insert - move
        # that element to the right
        while currentPosition > 0 and array[currentPosition - 1] > currentValue:
            array[currentPosition] = array[currentPosition -1]
            currentPosition = currentPosition - 1


        # We have either reached the beginning of the array or we have found
        # an element of the sorted array that is smaller than the element
        # we're trying to insert at index currentPosition - 1.
        # Either way - we insert the element at currentPosition
        array[currentPosition] = currentValue

    return array

print(insertion_sort(przyklad))