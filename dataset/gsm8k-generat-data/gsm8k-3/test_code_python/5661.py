def solution():
    """The civic league was hosting a pancake breakfast fundraiser.  A stack of pancakes was $4.00 and you could add bacon for $2.00.  They sold 60 stacks of pancakes and 90 slices of bacon.  How much did they raise?"""
    # Define the price of a stack of pancakes and a slice of bacon
    PANCAKE_PRICE = 4.00
    BACON_PRICE = 2.00

    # Define the number of stacks of pancakes and slices of bacon sold
    pancake_stacks = 60
    bacon_slices = 90

    # Calculate the total amount raised
    pancake_sales = pancake_stacks * PANCAKE_PRICE
    bacon_sales = bacon_slices * BACON_PRICE
    total_sales = pancake_sales + bacon_sales

    # Display the total amount raised
    result = total_sales
    return result

print(solution())