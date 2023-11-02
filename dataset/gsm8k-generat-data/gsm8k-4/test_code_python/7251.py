def solution():
    """Melissa sells a coupe for $30,000 and an SUV for twice as much. If her commission is 2%, how much money did she make from these sales?"""
    # Define the prices of the coupe and SUV
    coupe_price = 30000
    suv_price = coupe_price * 2

    # Calculate Melissa's commission for each car
    coupe_commission = coupe_price * 0.02
    suv_commission = suv_price * 0.02

    # Calculate the total amount of money Melissa made from these sales
    total_commission = coupe_commission + suv_commission

    result = total_commission
    return result

print(solution())