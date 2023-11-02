def solution():
    meat_cost = 17
    chicken_cost = 22
    veggies_cost = 43
    eggs_cost = 5
    dog_food_cost = 45
    end_balance = 35

    # Calculate the total cost of all groceries
    total_grocery_cost = meat_cost + chicken_cost + veggies_cost + eggs_cost + dog_food_cost

    # Calculate how much money Trisha had at the beginning
    initial_balance = total_grocery_cost + end_balance
    result = initial_balance
    return result

print(solution())