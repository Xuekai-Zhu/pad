def solution():
    """Ivy drinks 2.5 liters of water each day. How many bottles of 2-liter water should Ivy buy for her 4 days consumption?"""
    # Define Ivy's daily water consumption and number of days
    daily_consumption = 2.5 # liters
    num_days = 4

    # Calculate Ivy's total water consumption over 4 days
    total_consumption = daily_consumption * num_days # liters

    # Calculate how many 2-liter bottles Ivy needs to buy
    num_bottles = total_consumption / 2 # bottles

    # Round up to the nearest whole number of bottles
    num_bottles = math.ceil(num_bottles)

    # Display the number of bottles Ivy needs to buy
    result = num_bottles
    return result

print(solution())