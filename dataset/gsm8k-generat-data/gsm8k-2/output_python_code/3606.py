def solution():
    """In India, it cost $1 to purify a gallon of fresh water. Each person needs 1/2 a gallon of fresh water a day. In a family of 6, how much will it cost for fresh water for the day?"""
    cost_per_gallon = 1
    gallons_needed = 6 * 0.5
    total_cost = cost_per_gallon * gallons_needed
    result = total_cost
    return result

print(solution())