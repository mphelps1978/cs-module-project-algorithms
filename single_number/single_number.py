'''
Input: a List of integers where every int except one shows up twice
Returns: an integer

********************************************************************

We need to sort the array first and foremost, so that we can get all of the like numbers together
We can set up a hashtable to track whether we've seen the number or not..
    The hashtable will have the same structure as the list, so for example:
        [1, 2, 1, 3, 4, 3, 5, 2, 5]
        Sorted would be
        [1,1,2,2,3,3,4,5,5]

        Our hashtable would look like this:
        { 1: 0, 2: 0, 3: 0, 4: 0, 5: 0}

then we can loop through the array:
    if the number is in the array, we can increment the value of the index in the hashtable,
    and if it's not, we add it to the table

     so using the above example,
    as we're looping through
    [1,1,2,2,3,3,4,5,5]

    we get this..
    { 1: 2, 2:2 , 3: 2, 4: 1, 5: 2}
    we then loop over the hashtable
    and return the key of the item that has a value of 1


'''


def single_number(arr):
    # arr.sort()
    tracker = {}

    for i in range(len(arr)):
        if arr[i] in tracker:
            tracker[arr[i]] += 1

        else:
            tracker[arr[i]] = 1

    for item in tracker:
        if tracker[item] == 1:
            return item


if __name__ == '__main__':
    # Use the main function to test your implementation
    arr = [1, 1, 4, 4, 5, 5, 3, 3, 9, 0, 0]

    print(f"The odd-number-out is {single_number(arr)}")
