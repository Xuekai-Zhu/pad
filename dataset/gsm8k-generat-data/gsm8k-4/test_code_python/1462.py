def solution():
    """A candy store uses food colouring in various candies. Each lollipop uses 5ml of food colouring, and each hard candy also needs food colouring. In one day, the candy store makes 100 lollipops and 5 hard candies. They do not use food colouring in anything else. The store has used 600ml of food colouring by the end of the day. How much food colouring, in millilitres, does each hard candy need?"""
    # Define the amount of food colouring used for each lollipop
    lollipop_colouring = 5

    # Define the total number of lollipops and hard candies made
    lollipops = 100
    hard_candies = 5

    # Calculate the total amount of food colouring used for the lollipops
    lollipop_colouring_total = lollipops * lollipop_colouring

    # Calculate the total amount of food colouring used for the hard candies
    hard_candy_colouring_total = 600 - lollipop_colouring_total

    # Calculate the amount of food colouring used for each hard candy
    hard_candy_colouring = hard_candy_colouring_total / hard_candies

    # Return the result
    result = hard_candy_colouring
    return result

print(solution())