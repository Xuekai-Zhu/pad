def solution():
    """Edward had $17.80 to spend at the toy store. He bought 4 toy cars that cost $0.95 each and a race track that cost $6.00. How much money does Edward have left to buy more toys?"""
    # Define the initial amount of money and the cost of the items purchased
    initial_amount = 17.80
    car_cost = 0.95
    race_track_cost = 6.00

    # Calculate the total cost of the items purchased
    total_cost = (4 * car_cost) + race_track_cost

    # Calculate the amount of money Edward has left
    remaining_amount = initial_amount - total_cost

    # Return the result
    result = remaining_amount
    return result

print(solution())