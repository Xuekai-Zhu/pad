def solution():
    regular_price = 8
    discount_price = regular_price - 3
    num_people = 5   # Kath's 2 siblings and 3 friends
    total_cost = (num_people * discount_price)   # Costs before 6 PM
    result = total_cost
    return result

print(solution())