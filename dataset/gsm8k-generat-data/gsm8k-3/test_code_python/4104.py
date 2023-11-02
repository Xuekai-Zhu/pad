def solution():
    """Annie goes to school. Today is her birthday, so Annie decided to buy some sweets for her colleagues. Every classmate got 2 candies. In the end, Annie got left with 12 candies. If there are 35 people in Annie's class in total, how much did Annie spend on candies, if one candy costs $0.1?"""
    # Define the number of candies that Annie gave away
    candies_given = 35 * 2 - 12

    # Calculate the total cost of the candies
    cost = candies_given * 0.1

    # Display the total cost
    result = cost
    return result

print(solution())