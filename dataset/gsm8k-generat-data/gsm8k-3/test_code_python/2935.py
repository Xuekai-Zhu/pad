def solution():
    """Edward had $17.80 to spend at the toy store. He bought 4 toy cars that cost $0.95 each and a race track that cost $6.00. How much money does Edward have left to buy more toys?"""
    # Define the cost of the toy cars and the race track
    TOY_CAR_COST = 0.95
    RACE_TRACK_COST = 6.00

    # Define the number of toy cars purchased
    num_toy_cars = 4

    # Calculate the total cost of the toy cars
    total_toy_cars_cost = num_toy_cars * TOY_CAR_COST

    # Calculate the total cost of the purchase
    total_purchase_cost = total_toy_cars_cost + RACE_TRACK_COST

    # Calculate the remaining amount of money
    remaining_money = 17.80 - total_purchase_cost

    # Display the remaining amount of money
    result = remaining_money
    return result

print(solution())