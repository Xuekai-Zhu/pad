def solution():
    """Alex is saving up for a new car. He already has $14,500 saved up and the car costs $14,600. He decides that to make the last of the money he will deliver groceries for people in the neighborhood. He charges $1.5 per trip and then 5% of the price of the groceries. If he makes 40 trips and has saved up enough, how many dollars' worth of groceries did he deliver?"""
    # Define the initial amount Alex has saved and the price of the car
    initial_savings = 14500
    car_price = 14600

    # Define the earnings per grocery delivery and the number of deliveries Alex needs to make
    earnings_per_delivery = 1.5
    num_deliveries = 40

    # Calculate the total earnings from grocery deliveries
    grocery_earnings = earnings_per_delivery * num_deliveries

    # Calculate the total cost of the car, including 5% of the price of the groceries
    total_cost = car_price - initial_savings - grocery_earnings - (0.05 * grocery_earnings)

    # Calculate the value of the groceries Alex delivered
    grocery_value = (total_cost - earnings_per_delivery * num_deliveries) / 0.05

    # Return the result
    result = grocery_value
    return result

print(solution())