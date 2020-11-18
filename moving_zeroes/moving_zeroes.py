'''
Input: a List of integers
Returns: a List of integers

****************************************************

We want to move all of the non-zero integers to the left side of the list

The easiest way seems to be to create a new list, adding the items in,
unless it's a zero. We keep track of the number of 0s

once we get through the list, we can append the
tracked number of 0s to the end

'''


def moving_zeroes(arr):
    zero_tracker = 0
    newList = []

    for i in range(len(arr)):
        if arr[i] == 0:
            zero_tracker += 1
        else:
            newList.append(arr[i])

    for i in range(zero_tracker):
        newList.append(0)

    return newList


if __name__ == '__main__':
    # Use the main function here to test out your implementation
    arr = [0, 3, 1, 0, -2]

    print(f"The resulting of moving_zeroes is: {moving_zeroes(arr)}")
