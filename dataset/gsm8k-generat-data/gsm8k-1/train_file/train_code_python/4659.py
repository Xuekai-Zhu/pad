def solution():
    """Alex is saving up for a new car. He already has $14,500 saved up and the car costs $14,600. He decides that to make the last of the money he will deliver groceries for people in the neighborhood. He charges $1.5 per trip and then 5% of the price of the groceries. If he makes 40 trips and has saved up enough, how many dollars' worth of groceries did he deliver?"""
    savings = 14500
    car_cost = 14600
    trips = 40
    fee_per_trip = 1.5
    fee_percent = 0.05
    total_fees = trips * fee_per_trip
    groceries = (car_cost - savings - total_fees)/(fee_percent)
    result = groceries
    return result

print(solution())