def solution():
    # Define the number of cakes and the cost per cake
    num_cakes = 3
    cost_per_cake = 12

    # Calculate the total cost for the cakes
    total_cost = num_cakes * cost_per_cake

    # Divide the total cost by 2 since John is splitting the cost with his brother
    john_paid = total_cost / 2
    result = john_paid
    return result

print(solution())