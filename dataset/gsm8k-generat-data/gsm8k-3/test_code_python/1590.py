def solution():
    """John used to buy 4 coffees a day for $2 each. They raised the price by 50% so he cut the number of coffees he drinks in half. How much money does he save per day compared to what he used to spend?"""
    # Define the original price per coffee and the new price after the increase
    ORIGINAL_PRICE = 2
    NEW_PRICE = ORIGINAL_PRICE * 1.5

    # Define the original number of coffees and the new number after John cuts back
    ORIGINAL_COFFEES = 4
    NEW_COFFEES = ORIGINAL_COFFEES / 2

    # Calculate the total amount John used to spend and the new total after the price increase
    ORIGINAL_TOTAL = ORIGINAL_PRICE * ORIGINAL_COFFEES
    NEW_TOTAL = NEW_PRICE * NEW_COFFEES

    # Calculate the amount John saves per day compared to what he used to spend
    SAVINGS = ORIGINAL_TOTAL - NEW_TOTAL

    # Display the amount of money John saves per day
    result = SAVINGS
    return result

print(solution())