def solution():
    # Define constants for package size and price
    PACKAGE_SIZE = 200
    WHITE_PRICE = 5
    SWISS_PRICE = 6
    BLUE_PRICE = 8

    # Calculate the amount of each cheese Miley needs to buy
    swiss_amount = 5 * PACKAGE_SIZE
    blue_amount = 600
    white_amount = 4/3 * swiss_amount

    # Calculate the total cost of each type of cheese
    white_cost = white_amount/PACKAGE_SIZE * WHITE_PRICE
    swiss_cost = swiss_amount/PACKAGE_SIZE * SWISS_PRICE
    blue_cost = blue_amount/PACKAGE_SIZE * BLUE_PRICE

    # Calculate the total cost for all the cheese
    total_cost = white_cost + swiss_cost + blue_cost
    result = total_cost
    return result

print(solution())