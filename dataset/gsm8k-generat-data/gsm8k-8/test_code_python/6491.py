def solution():
    # Define the cost of the first 100 channels and the cost of the next 100 channels
    cost_100 = 100
    cost_next_100 = cost_100 / 2

    # Calculate the total cost of the cable program
    total_cost = cost_100 + cost_next_100

    # Divide the total cost by 2 for the split with his roommate
    james_paid = total_cost / 2
    result = james_paid
    return result

print(solution())