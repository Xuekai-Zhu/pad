def solution():
    # Define the number of t-shirts and pants bought
    t_shirts = 5
    pants = 4

    # Calculate the total cost of t-shirts
    t_shirt_cost = t_shirts * 100

    # Calculate the remaining amount for pants
    pants_cost = 1500 - t_shirt_cost

    # Calculate the cost of each pair of pants
    pants_price = pants_cost / pants
    result = pants_price
    return result

print(solution())