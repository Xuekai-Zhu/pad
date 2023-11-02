def solution():
    
    starting_money = 120
    hamburgers = 8
    hamburgers_price = 4
    milkshakes = 6
    milkshakes_price = 3
    total_spent = hamburgers * hamburgers_price + milkshakes * milkshakes_price
    remaining_money = starting_money - total_spent
    result = remaining_money
    return result

print(solution())