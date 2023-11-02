def solution():
    """Theodore can craft 10 stone statues and 20 wooden statues every month. A stone statue costs $20 and a wooden statue costs $5. He also pays 10 percent of his total earnings in taxes. How much is his total earning every month?"""
    # Define the number of stone and wooden statues crafted per month
    STONE_STATUES = 10
    WOODEN_STATUES = 20

    # Define the cost of each type of statue
    STONE_PRICE = 20
    WOODEN_PRICE = 5

    # Calculate the total revenue from the stone statues
    stone_revenue = STONE_STATUES * STONE_PRICE

    # Calculate the total revenue from the wooden statues
    wooden_revenue = WOODEN_STATUES * WOODEN_PRICE

    # Calculate the total revenue from all the statues
    total_revenue = stone_revenue + wooden_revenue

    # Calculate the amount of tax that Theodore needs to pay
    tax = total_revenue * 0.1

    # Calculate Theodore's total earnings after taxes
    earnings = total_revenue - tax

    # Display Theodore's total earnings
    result = earnings
    return result

print(solution())