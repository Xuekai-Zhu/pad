def solution():
    # Define the number of boxes sold to each customer
    customer1 = 5
    customer2 = 4 * customer1
    customer3 = 0.5 * customer2
    customer4 = 3 * customer3
    customer5 = 10

    # Calculate the total number of boxes sold
    total_sold = customer1 + customer2 + customer3 + customer4 + customer5

    # Calculate the number of boxes Jill needs to sell to hit her goal
    goal = 150
    boxes_left = goal - total_sold
    result = boxes_left
    return result

print(solution())