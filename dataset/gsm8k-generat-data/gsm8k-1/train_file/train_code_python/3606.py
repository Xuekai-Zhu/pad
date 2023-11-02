def solution():
    """In India, it cost $1 to purify a gallon of fresh water. Each person needs 1/2 a gallon of fresh water a day. In a family of 6, how much will it cost for fresh water for the day?"""
    cost_per_gallon = 1
    gallons_per_person = 0.5
    num_people = 6
    total_gallons = gallons_per_person * num_people
    total_cost = total_gallons * cost_per_gallon
    result = total_cost
    return result

print(solution())