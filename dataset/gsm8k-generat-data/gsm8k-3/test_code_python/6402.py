def solution():
    """Julio makes a mocktail every evening. He uses 1 tablespoon of lime juice and tops with 1 cup of sparkling water. He can usually squeeze 2 tablespoons of lime juice per lime. After 30 days, if limes are 3 for $1.00, how much will he have spent on limes?"""
    # Define the number of limes needed per day
    limes_per_day = 1 / 2  # 1 tablespoon = 1/2 lime

    # Define the number of days in a month
    days_in_month = 30

    # Define the cost per lime
    cost_per_lime = 1 / 3  # 3 for $1.00

    # Calculate the total number of limes needed for the month
    total_limes = limes_per_day * days_in_month

    # Calculate the total cost of the limes
    total_cost = total_limes * cost_per_lime

    # Display the total cost of the limes
    result = total_cost
    return result

print(solution())