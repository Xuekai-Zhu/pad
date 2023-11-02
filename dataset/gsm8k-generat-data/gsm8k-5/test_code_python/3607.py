def solution():
    cost_per_gallon = 1  # It costs $1 to purify a gallon of fresh water
    water_per_person = 1/2  # Each person needs 1/2 a gallon of fresh water a day
    family_members = 6  # There are 6 people in the family

    # Calculate the total amount of fresh water needed for the family per day
    total_water_needed = water_per_person * family_members

    # Calculate the total cost for fresh water for the day
    total_cost = cost_per_gallon * total_water_needed
    result = total_cost
    return result

print(solution())