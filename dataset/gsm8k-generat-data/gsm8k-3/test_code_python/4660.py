def solution():
    """Alex is saving up for a new car. He already has $14,500 saved up and the car costs $14,600. He decides that to make the last of the money he will deliver groceries for people in the neighborhood.  He charges $1.5 per trip and then 5% of the price of the groceries. If he makes 40 trips and has saved up enough, how many dollars' worth of groceries did he deliver?"""
    # Define the cost of the car and the amount already saved
    CAR_PRICE = 14600
    SAVINGS = 14500

    # Define the cost per trip and the percentage charged on groceries
    TRIP_COST = 1.5
    GROCERY_PERCENT = 0.05

    # Define the number of trips made
    num_trips = 40

    # Calculate the total cost of the trips and groceries needed
    total_cost = CAR_PRICE - SAVINGS
    total_trips_cost = num_trips * TRIP_COST
    total_groceries_cost = (total_cost - total_trips_cost) / GROCERY_PERCENT

    # Display the total amount of groceries delivered
    result = total_groceries_cost
    return result

print(solution())