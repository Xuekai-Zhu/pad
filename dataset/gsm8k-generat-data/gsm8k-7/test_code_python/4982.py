def solution():
    lee_money = 10
    friend_money = 8
    chicken_wings_cost = 6
    chicken_salad_cost = 4
    soda_cost = 1
    num_sodas = 2
    tax = 3

    # Calculate the total amount spent on food and sodas
    total_food_cost = chicken_wings_cost + chicken_salad_cost + (soda_cost * num_sodas)

    # Calculate the total amount of money Lee and his friend had
    total_money = lee_money + friend_money

    # Calculate the total amount spent (including tax)
    total_spent = total_food_cost + tax

    # Calculate the total change received
    total_change = total_money - total_spent
    result = total_change
    return result

print(solution())