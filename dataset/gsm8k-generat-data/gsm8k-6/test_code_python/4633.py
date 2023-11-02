def solution():
    # Calculate the total cost of the meal
    meal_cost = (2*3.65) + 2 + 1 + 4 + (3*0.5) + 0.2  # cost of the two cheeseburgers, milkshake, coke, fries, and three cookies plus tax
    total_cost = meal_cost / 2  # split the bill evenly between Toby and his friend

    # Calculate the change Toby would get back
    change = 15 - total_cost
    result = change
    return result

print(solution())