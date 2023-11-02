def solution():
    """At the beginning of the day there were 74 apples in a basket. If Ricki removes 14 apples and Samson removes twice as many as Ricki. How many apples are left in the basket by the end of the day?"""
    # Define the initial number of apples in the basket
    num_apples = 74

    # Ricki removes 14 apples
    num_apples -= 14

    # Samson removes twice as many as Ricki
    num_apples -= 2 * 14

    # The number of apples left in the basket
    num_left = num_apples

    # return the result
    result = num_left
    return result

print(solution())