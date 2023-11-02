def solution():
    dresses = 5
    pants = 3
    jackets = 4
    transportation = 5
    dress_cost = 20
    pants_cost = 12
    jacket_cost = 30
    total_cost = (dresses * dress_cost) + (pants * pants_cost) + (jackets * jacket_cost) + transportation
    initial_amount = 400
    remaining_amount = initial_amount - total_cost
    result = remaining_amount
    return result

print(solution())