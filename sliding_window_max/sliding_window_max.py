'''
Input: a List of integers as well as an integer `k` representing the size of the sliding window
Returns: a List of integers

- Track the length of the input array
- Track the maximum value from each k window while traversing the array
- Track all of the answers we want to return

Loop through the array outside of the k window and
update the maximum value to the current element in the array

Add the maximum value to the answers array





'''


def sliding_window_max(nums, k):
    l = len(nums)
    mv = 0
    answer = []

    for i in range(l - k + 1):
        mv = nums[i]

        for j in range(1, k):
            if nums[i + j] > mv:
                mv = nums[i + j]

        answer.append(mv)

    return answer


if __name__ == '__main__':
    # Use the main function here to test out your implementation
    arr = [1, 3, -1, -3, 5, 3, 6, 7]
    k = 3

    print(f"Output of sliding_window_max function is: {sliding_window_max(arr, k)}")
