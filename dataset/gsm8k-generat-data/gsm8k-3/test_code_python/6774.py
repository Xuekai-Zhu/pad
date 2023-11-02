def solution():
    """At a certain car dealership, 15% of the cars cost less than $15000 and 40% of the cars cost more than $20000. If there are 3000 cars at the dealership, how many of them cost between $15000 and $20000?"""
    # Calculate the number of cars that cost less than $15000
    less_than_15k = 0.15 * 3000

    # Calculate the number of cars that cost more than $20000
    more_than_20k = 0.40 * 3000

    # Calculate the number of cars that cost between $15000 and $20000
    between_15k_and_20k = 3000 - less_than_15k - more_than_20k

    # Display the number of cars that cost between $15000 and $20000
    result = between_15k_and_20k
    return result

print(solution())