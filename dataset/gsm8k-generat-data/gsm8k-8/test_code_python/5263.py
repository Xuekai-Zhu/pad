def solution():
    # Define the cost of the car and the number of days in a week
    car_cost = 2100
    days_in_week = 7

    # Calculate the percentage of days each person will use the car
    sister_days = 4
    sue_days = days_in_week - sister_days
    sister_percent = sister_days / days_in_week
    sue_percent = sue_days / days_in_week

    # Calculate how much each person will pay based on their percentage of use
    sister_payment = sister_percent * car_cost
    sue_payment = sue_percent * car_cost

    result = sue_payment
    return result

print(solution())