def solution():
    
    bacon_price = 10
    chicken_price = bacon_price * 2
    strawberry_price = 4
    apple_price = strawberry_price / 2
    total_budget = 65
    bacon_total = bacon_price * 5
    chicken_total = chicken_price * 6
    strawberry_total = strawberry_price * 3
    apple_total = apple_price * 7
    total_cost = bacon_total + chicken_total + strawberry_total + apple_total
    remaining_budget = total_budget - total_cost
    result = remaining_budget
    return result

print(solution())