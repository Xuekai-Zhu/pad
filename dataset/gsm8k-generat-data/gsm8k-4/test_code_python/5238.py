def solution():
    """For every 12 cans you recycle, you receive $0.50, and for every 5 kilograms of newspapers, you receive $1.50. If your family collected 144 cans and 20 kilograms of newspapers, how much money would you receive?"""
    # Define the prices for recycling cans and newspapers
    CAN_PRICE = 0.5 / 12
    NEWSPAPER_PRICE = 1.5 / 5

    # Calculate the total amount received for recycling cans
    can_money = CAN_PRICE * 144

    # Calculate the total amount received for recycling newspapers
    newspaper_money = NEWSPAPER_PRICE * 20

    # Calculate the total amount received
    total_money = can_money + newspaper_money

    # return the result
    result = total_money
    return result

print(solution())