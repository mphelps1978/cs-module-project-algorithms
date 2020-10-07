"""
We'll say that a positive int divides itself if every digit in the number
divides into the number evenly. So for example 128 divides itself since 1, 2,
and 8 all divide into 128 evenly.
​
And we'll say that 0 does not divide into anything evenly, so no number with a
0 digit divides itself.
​
Write a function to determine if a number divides itself.
​
*********************************************************************************

Is there a possibility of floating points? <-- Integer Only, No Floating Points or Strings
Will it only be a single number? Or could it be a list of numbers? <-- Single only
Can the ints be positive/negative? <-- Either


Given a positive or negative fixed point integer,
determine if the number can divide itself.
0 does not divides itself
Take in a single input arg
return a Boolean based on the result

"""

# depending on the length of the number, we need to split it into a list
# then take the individual numbers
# Loop through them and see if they devide evenly (% = 0)


def divides_itself(number):

    digits = list(str(number))

    # 0 Case
    if number is 0:
        return False
