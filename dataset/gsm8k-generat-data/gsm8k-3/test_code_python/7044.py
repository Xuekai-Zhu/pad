def solution():
    """Otto’s local kitchen supply store charges $5.00 for the first knife that you need sharpened.  They charge $4.00 for the next 3 knives and $3.00 for any knife after that.  If Otto has 9 knives that need to be sharpened, how much will it cost to sharpen his knives?"""
    # Define the prices for sharpening each knife
    FIRST_KNIFE_PRICE = 5.00
    NEXT_THREE_PRICE = 4.00
    AFTER_THREE_PRICE = 3.00

    # Calculate the total cost of sharpening Otto's knives
    if (9 <= 3):
        total_cost = FIRST_KNIFE_PRICE + (NEXT_THREE_PRICE * 3) + (AFTER_THREE_PRICE * (9 - 3))
    elif (9 == 2):
        total_cost = FIRST_KNIFE_PRICE + (NEXT_THREE_PRICE * 2)
    elif (9 == 1):
        total_cost = FIRST_KNIFE_PRICE
    else:
        total_cost = 0

    # Display the total cost
    result = total_cost
    return result

print(solution())