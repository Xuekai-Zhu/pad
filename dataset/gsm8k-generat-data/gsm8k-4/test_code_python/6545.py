def solution():
    """James decides to start making his own coffee. He buys a coffee machine for $200 and gets a $20 discount. He figures it will cost him $3 a day to make his coffee. He previously bought 2 coffees a day for $4 each. How long until the machine pays for itself?"""
    # Define the cost of the coffee machine and the discount received
    machine_cost = 200
    discount = 20

    # Calculate the total cost of the machine after the discount
    total_cost = machine_cost - discount

    # Calculate the savings per day from making his own coffee
    coffee_savings = 2 * 4 - 3 * 2

    # Calculate the number of days it will take for the machine to pay for itself
    days = total_cost / coffee_savings

    # Round up to the nearest integer number of days
    days = math.ceil(days)

    result = days
    return result

print(solution())