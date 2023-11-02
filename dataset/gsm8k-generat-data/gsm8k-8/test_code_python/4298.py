def solution():
    # Define the prices and the amounts bought
    potatoes_price = 2
    potatoes_amount = 6
    tomatoes_price = 3
    tomatoes_amount = 9
    cucumbers_price = 4
    cucumbers_amount = 5
    bananas_price = 5
    bananas_amount = 3

    # Calculate the total amount spent
    total_spent = (potatoes_price * potatoes_amount +
                   tomatoes_price * tomatoes_amount +
                   cucumbers_price * cucumbers_amount + 
                   bananas_price * bananas_amount)

    # Calculate Peter's remaining money
    remaining_money = 500 - total_spent
    result = remaining_money
    return result

print(solution())