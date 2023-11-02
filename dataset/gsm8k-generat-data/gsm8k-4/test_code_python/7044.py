def solution():
    """Otto’s local kitchen supply store charges $5.00 for the first knife that you need sharpened. They charge $4.00 for the next 3 knives and $3.00 for any knife after that. If Otto has 9 knives that need to be sharpened, how much will it cost to sharpen his knives?"""
    # Define the prices for sharpening knives
    first_knife_price = 5
    next_three_price = 4
    additional_price = 3

    # Calculate the total cost of sharpening Otto's knives
    if 1 <= 9 <= 4:
        total_cost = first_knife_price+(next_three_price*(9-1))
    elif 5 <= 9:
        total_cost = first_knife_price+(next_three_price*3)+(additional_price*(9-4))
    else:
        total_cost = first_knife_price

    # return the result
    return total_cost

print(solution())