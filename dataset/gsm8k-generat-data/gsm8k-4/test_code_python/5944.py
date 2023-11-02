def solution():
    """A farmer is checking his fields to make sure all of his crops are growing as they should. Rows of corn stalks should produce 9 corn cobs each, and rows of potatoes should produce 30 potatoes each. As he’s checking crop quality, he notices that there are more pests than usual and they have destroyed some of his crops. He thinks that half of his crops have been destroyed by the pests. If the farmer has 10 rows of corn stalks and 5 rows of potatoes, how many crops does the farmer still have?"""
    # Define the number of rows of corn stalks and potatoes
    corn_rows = 10
    potato_rows = 5

    # Define the expected yield per row of corn and potatoes
    corn_yield = 9
    potato_yield = 30

    # Calculate the total number of crops before pest damage
    total_crops = (corn_rows * corn_yield) + (potato_rows * potato_yield)

    # Calculate the number of crops destroyed by pests
    destroyed_crops = total_crops / 2

    # Calculate the number of crops remaining
    remaining_crops = total_crops - destroyed_crops

    result = remaining_crops
    return result

print(solution())