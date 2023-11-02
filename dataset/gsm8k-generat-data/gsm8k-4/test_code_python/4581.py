def solution():
    """Mr. Jesiah is a dairy cow farmer with cows producing 200 gallons of milk every day. The expenses for maintenance of the dairy farm and purchase of feeds is $3000 per month. Calculate his total income in June if he sells 1 gallon of milk at $3.55."""
    # Define the number of cows and the amount of milk produced per day
    cows = 200
    milk_per_day = 200 * cows

    # Calculate the total amount of milk produced in June
    days_in_june = 30
    milk_in_june = milk_per_day * days_in_june

    # Calculate the total income from selling milk in June
    price_per_gallon = 3.55
    total_income = milk_in_june * price_per_gallon

    # Calculate the total expenses for June
    expenses = 3000

    # Calculate the net income for June
    net_income = total_income - expenses

    # Return the net income
    result = net_income
    return result

print(solution())