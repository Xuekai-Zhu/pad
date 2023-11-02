def solution():
    # Define the cost of the cards in each box
    box1_cost = 1.25
    box2_cost = 1.75

    # Calculate the total cost of the cards bought from each box
    total_box1_cost = 6 * box1_cost
    total_box2_cost = 6 * box2_cost

    # Calculate the total cost of all the cards
    total_cost = total_box1_cost + total_box2_cost
    result = total_cost
    return result

print(solution())