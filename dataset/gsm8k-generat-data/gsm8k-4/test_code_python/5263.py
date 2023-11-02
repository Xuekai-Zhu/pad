def solution():
    """Sue and her sister buy a $2,100 car. They agree to split the cost based on the percentage of days use. Sue's sister will drive the car 4 days a week and Sue will get the rest of the days. How much does Sue have to pay?"""
    # Define the total cost of the car
    total_cost = 2100

    # Define the number of days each sister will use the car
    sister_days = 4 * 7  # 4 days a week for 7 days
    sue_days = (7 - 4) * 7  # the rest of the days in a week for 7 days

    # Calculate the percentage of days each sister will use the car
    sister_percentage = sister_days / 49  # 7 days x 7 weeks
    sue_percentage = sue_days / 49

    # Calculate how much each sister should pay
    sister_payment = total_cost * sister_percentage
    sue_payment = total_cost * sue_percentage

    # Calculate how much Sue should pay
    sue_share = sue_payment

    result = sue_share
    return result

print(solution())