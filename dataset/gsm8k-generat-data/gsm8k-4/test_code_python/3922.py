def solution():
    """A car manufacturing company that produces 100 cars per month wants to increase its production to reach 1800 cars per year. How many cars should the company add to the monthly production rate to reach that target?"""
    # Define the current monthly production rate and the desired yearly production rate
    current_production = 100
    desired_production = 1800

    # Calculate the additional cars needed per month to reach the desired yearly production rate
    additional_cars = (desired_production - (current_production * 12)) / 12

    # Round up to the nearest integer
    additional_cars = math.ceil(additional_cars)

    # Display the result
    result = additional_cars
    return result

print(solution())