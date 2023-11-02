def solution():
    """In India, it cost $1 to purify a gallon of fresh water. Each person needs 1/2 a gallon of fresh water a day. In a family of 6, how much will it cost for fresh water for the day?"""
    # Define the cost to purify a gallon of fresh water and the number of people in the family
    COST_PER_GALLON = 1
    FAMILY_SIZE = 6

    # Calculate the total gallons of fresh water needed for the family for the day
    total_gallons = FAMILY_SIZE * 0.5

    # Calculate the total cost to purify the fresh water for the family for the day
    total_cost = total_gallons * COST_PER_GALLON

    # return the result
    result = total_cost
    return result

print(solution())