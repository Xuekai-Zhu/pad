def solution():
    """Sue and her sister buy a $2,100 car. They agree to split the cost based on the percentage of days use. Sue's sister will drive the car 4 days a week and Sue will get the rest of the days. How much does Sue have to pay?"""
    # Define the cost of the car
    car_cost = 2100

    # Calculate the number of days each person will use the car
    sister_days = 4 * 7
    sue_days = 7 * (1 - 4/7)

    # Calculate the percentage of the cost each person will pay
    sister_percent = sister_days / (sister_days + sue_days)
    sue_percent = 1 - sister_percent

    # Calculate how much each person will pay
    sister_payment = sister_percent * car_cost
    sue_payment = sue_percent * car_cost

    # Display how much Sue has to pay
    result = sue_payment
    return result

print(solution())