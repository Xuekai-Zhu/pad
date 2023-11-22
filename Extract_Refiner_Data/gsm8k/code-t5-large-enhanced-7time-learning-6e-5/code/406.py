def solution():
    
    # Define the initial amount of money Sally has
    initial_money = 10

    # Calculate the cost of the taffy's purchase
    taffy_cost = 3 * 0.5

    # Calculate the cost of the purchases
    purchases = 2 + 1.5 + 0.25

    # Calculate the total cost of the purchase
    total_cost = taffy_cost + purchases

    # Calculate the amount of money Sally has left
    money_left = initial_money - total_cost

    # Display the amount of money Sally has left
    result = money_left
    return result

print(solution())