def solution():
    """In a stationery store, there are three kinds of pencils. A pencil with an eraser, which costs $0.8 each, a regular pencil for $0.5 each, and a short pencil for $0.4 each. This store was able to sell 200 pencils with an eraser, 40 regular pencils, and 35 short pencils. How much money did the store make from these sales?"""
    # Define the prices of each type of pencil
    ERASER_PRICE = 0.8
    REGULAR_PRICE = 0.5
    SHORT_PRICE = 0.4

    # Define the number of each type of pencil sold
    eraser_count = 200
    regular_count = 40
    short_count = 35

    # Calculate the total money made from selling each type of pencil
    eraser_money = eraser_count * ERASER_PRICE
    regular_money = regular_count * REGULAR_PRICE
    short_money = short_count * SHORT_PRICE

    # Calculate the total money made from all pencil sales
    total_money = eraser_money + regular_money + short_money

    # Display the total money made
    result = total_money
    return result

print(solution())