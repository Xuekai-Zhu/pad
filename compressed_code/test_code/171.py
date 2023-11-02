def solution():
    
    starting_amount = 5000
    motorcycle_cost = 2800
    concert_cost = (starting_amount - motorcycle_cost) / 2
    remaining_amount = starting_amount - motorcycle_cost - concert_cost
    lost_amount = remaining_amount / 4
    final_amount = remaining_amount - lost_amount
    result = final_amount
    return result

print(solution())