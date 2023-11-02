def solution():
    """In India, it cost $1 to purify a gallon of fresh water. Each person needs 1/2 a gallon of fresh water a day. In a family of 6, how much will it cost for fresh water for the day?"""
    # Define the cost to purify a gallon of water and the amount of water needed per person per day
    PURIFICATION_COST = 1
    WATER_PER_PERSON = 0.5

    # Calculate the total amount of fresh water needed for the family of 6
    total_water_needed = 6 * WATER_PER_PERSON

    # Calculate the total cost to purify this amount of fresh water
    total_cost = total_water_needed * PURIFICATION_COST

    # Display the total cost for fresh water for the day
    result = total_cost
    return result

print(solution())