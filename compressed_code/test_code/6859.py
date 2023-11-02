def solution():
    
    hamburgers_bought = 8
    hamburgers_price = 4
    milkshakes_bought = 6
    milkshakes_price = 5
    total_spent = (hamburgers_bought * hamburgers_price) + (milkshakes_bought * milkshakes_price) + 70
    total_money = total_spent
    return total_money

print(solution())