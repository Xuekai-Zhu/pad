def solution():
    """The news announced a $0.4 oil price rollback this Friday. Mr. Deane decided to only fill his gas tank with 10 liters of gas today and then another 25 liters on Friday. If the cost per liter of gas is $1.4 today, how much will Mr. Deane spend for his 35 liters of gas?"""
    # Define the cost per liter of gas today
    today_cost = 1.4

    # Define the number of liters of gas bought today and on Friday
    today_liters = 10
    friday_liters = 25

    # Calculate the cost of the gas bought today and on Friday
    today_cost = today_cost - 0.4
    today_cost_total = today_cost * today_liters
    friday_cost_total = today_cost * friday_liters

    # Calculate the total cost of gas bought
    total_cost = today_cost_total + friday_cost_total

    # Display the total cost
    result = total_cost
    return result

print(solution())