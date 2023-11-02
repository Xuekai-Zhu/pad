def solution():
    # Calculate the total cost of the dresses
    dress_cost = 5 * 20

    # Calculate the total cost of the pants
    pants_cost = 3 * 12

    # Calculate the total cost of the jackets
    jacket_cost = 4 * 30

    # Calculate the total cost of everything
    total_cost = dress_cost + pants_cost + jacket_cost + 5  # Adding $5 for transportation

    # Calculate how much money Rita has now
    remaining_money = 400 - total_cost
    result = remaining_money
    return result

print(solution())