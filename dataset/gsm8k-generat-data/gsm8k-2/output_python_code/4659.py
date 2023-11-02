def solution():
    """Alex is saving up for a new car. He already has $14,500 saved up and the car costs $14,600. He decides that to make the last of the money he will deliver groceries for people in the neighborhood. He charges $1.5 per trip and then 5% of the price of the groceries. If he makes 40 trips and has saved up enough, how many dollars' worth of groceries did he deliver?"""
    car_cost = 14600
    initial_savings = 14500
    trips = 40
    trip_fee = 1.5
    groceries_percentage = 0.05

    money_needed = car_cost - initial_savings
    total_groceries_cost = (money_needed - (trips * trip_fee)) / groceries_percentage
    result = total_groceries_cost
    return result

print(solution())