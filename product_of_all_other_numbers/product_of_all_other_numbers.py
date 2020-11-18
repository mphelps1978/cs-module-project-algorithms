'''
Input: a List of integers
Returns: a List of integers


**************************************************************************************
Write a function that receives an array of integers and returns an array consisting of the product of all numbers in the array _except_ the number at that index.

Example:
[1, 2, 3]

Would return
[6, 3, 2]

In this case, the final value at index 0 is the product of every number in the input array _except_ the number at index 0.


 - First, we should set a variable to the length of the input array <-- arr_length
 - Then we can create a list of answers, with the initial value of 0 for each element in the input (4 numbers = [0,0,0,0]) <-- answers = [] * arr_length
 - We should create a variable that initializes at 1, and holds the product of all of the elements to the right of the current element (1 because
   there is nothing to the right of the last element of the input)  <-- right_product

- Now we can then work with the list
    Our list of answers contains the product of all elements to the left. Since index 0 has
    nothing to the left, we can just set it's value to 1

    For every element in the array after that, we can calculate the value by multiplying
    the previous element with the element from the input array

    Next, reverse the input array, and calculate the new value by mulitplying current value * right_product value
        We can update the right_product value by multiplying it's valuye by the current element in the input array

Once answers is populated with all of the left side values and then updated by multiplying the right_product, we're done and can return aswers


EDGE CASES FROM TEST
    Input array has only 2 numbers... add them to answers, swapping positions
'''


def product_of_all_other_numbers(arr):
    arr_length = len(arr)
    answers = [0] * arr_length
    right_product = 1
    answers[0] = 1

    if arr_length == 2:
        answers[0], answers[1] = arr[1], arr[0]
        return answers

    for i in range(1, arr_length):
        answers[i] = answers[i - 1] * arr[i - 1]

    for i in reversed(range(arr_length)):
        answers[i] = answers[i] * right_product
        right_product *= arr[i]

    return answers


if __name__ == '__main__':
    # Use the main function to test your implementation
    # arr = [1, 2, 3, 4, 5]
    arr = [2, 6, 9, 8, 2, 2, 9, 10, 7, 4, 7, 1, 9, 5, 9, 1, 8, 1, 8, 6, 2, 6, 4, 8,
           9, 5, 4, 9, 10, 3, 9, 1, 9, 2, 6, 8, 5, 5, 4, 7, 7, 5, 8, 1, 6, 5, 1, 7, 7, 8]

    print(f"Output of product_of_all_other_numbers: {product_of_all_other_numbers(arr)}")
