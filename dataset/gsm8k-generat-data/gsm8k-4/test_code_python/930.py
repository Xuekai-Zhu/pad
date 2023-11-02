def solution():
    """How many apples did two men and three women buy at a certain store if the two men each bought 30 apples, 20 less than the number of apples bought by each woman?"""
    # Define the number of apples bought by each man
    apples_per_man = 30

    # Define the difference in the number of apples bought by each woman and each man
    apple_difference = 20

    # Calculate the number of apples bought by each woman
    apples_per_woman = apples_per_man + apple_difference

    # Calculate the total number of apples bought by the two men and three women
    total_apples = (2 * apples_per_man) + (3 * apples_per_woman)

    # return the result
    result = total_apples
    return result

print(solution())