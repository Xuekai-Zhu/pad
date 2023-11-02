def solution():
    number_of_bags = 2
    initial_price = 6
    discount_percent = 75
    discount_amount = initial_price * (discount_percent / 100)
    final_price = initial_price - discount_amount
    total_cost = number_of_bags * final_price
    result = total_cost
    return result

print(solution())