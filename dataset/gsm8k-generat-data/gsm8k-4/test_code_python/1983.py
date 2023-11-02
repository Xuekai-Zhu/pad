def solution():
    """Janet buys 3 pounds of broccoli for $4 a pound, 3 oranges for $0.75 each, a cabbage for $3.75, a pound of bacon for $3, and two pounds of chicken for $3 a pound. What percentage of her grocery budget did she spend on meat, rounded to the nearest percent?"""
    # Define the prices and quantities of each item
    broccoli_price = 4
    broccoli_quantity = 3
    orange_price = 0.75
    orange_quantity = 3
    cabbage_price = 3.75
    bacon_price = 3
    bacon_quantity = 1
    chicken_price = 3
    chicken_quantity = 2

    # Calculate the total cost of each item
    broccoli_cost = broccoli_price * broccoli_quantity
    orange_cost = orange_price * orange_quantity
    cabbage_cost = cabbage_price
    bacon_cost = bacon_price * bacon_quantity
    chicken_cost = chicken_price * chicken_quantity

    # Calculate the total cost of the groceries
    total_cost = broccoli_cost + orange_cost + cabbage_cost + bacon_cost + chicken_cost

    # Calculate the percentage of the budget spent on meat
    meat_cost = bacon_cost + chicken_cost
    meat_percentage = (meat_cost / total_cost) * 100

    # Round the percentage to the nearest percent
    rounded_percentage = round(meat_percentage)

    # return the result
    result = rounded_percentage
    return result

print(solution())