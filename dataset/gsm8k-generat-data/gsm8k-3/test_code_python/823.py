def solution():
    """At the beginning of the day there were 74 apples in a basket. If Ricki removes 14 apples and Samson removes twice as many as Ricki. How many apples are left in the basket by the end of the day?"""
    # Define the initial number of apples
    initial_apples = 74

    # Ricki removes 14 apples
    ricki_apples = 14
    remaining_apples = initial_apples - ricki_apples

    # Samson removes twice as many apples as Ricki
    samson_apples = 2 * ricki_apples
    remaining_apples -= samson_apples

    # Display the number of apples remaining
    result = remaining_apples
    return result

print(solution())