'''
Input: an integer
Returns: an integer


Cookie Monster can eat either 1, 2, or 3 cookies at a time.
If he were given a jar of cookies with `n` cookies inside of it,
how many ways could he eat all `n` cookies in the cookie jar?

could do this with recursion.. since we know that there's only 3 possible combinations

Need to set up some base cases:
    - if there's 0 cookies, he can't eat any, now can he?
    - if there's only one cookie, he can only eat 1 * 1, so 1 way
    - if there's 2 cookies, he can eat 1 * 1, or 1 * 2, so 2 ways
    - if there's 3 cookies, he can eat 1 * 1, 1 * 2 + 1, 3 * 1, or 2 * 1 + 1, so 4 ways

Once we've set those bases, we can recursively call the function, passing in the number in the jar, minus one of the options (1 2 or 3)
and add all of those together

'''

# Unoptimized..

# def eating_cookies(n):
#     if n <= 1:
#         return 1
#     elif n == 2:
#         return 2
#     elif n == 3:
#         return 4
#     else:
#         return eating_cookies(n - 3) + eating_cookies(n - 2) + eating_cookies(n - 1)


def eating_cookies(n, cache=None):
    print(n)
    # base case: when there are no more cookies
    if n == 0:
        return 1
    # check for negative n values
    elif n < 0:
        return 0
    # add a case to have us check the cache
    elif cache and cache[n] > 0:
        return cache[n]
    # init our cache if we don't have it yet
    else:
        if not cache:
            cache = [0 for _ in range(n + 1)]
        # we can go ahead and save our answer to the cache
        cache[n] = eating_cookies(n - 1, cache) + eating_cookies(n - 2, cache) + eating_cookies(n - 3, cache)
    return cache[n]


if __name__ == "__main__":
    # Use the main function here to test out your implementation
    num_cookies = 5

    print(f"There are {eating_cookies(num_cookies)} ways for Cookie Monster to each {num_cookies} cookies")
