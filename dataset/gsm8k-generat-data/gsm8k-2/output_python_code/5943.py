def solution():
    """A farmer is checking his fields to make sure all of his crops are growing as they should. Rows of corn stalks should produce 9 corn cobs each, and rows of potatoes should produce 30 potatoes each. As he’s checking crop quality, he notices that there are more pests than usual and they have destroyed some of his crops. He thinks that half of his crops have been destroyed by the pests. If the farmer has 10 rows of corn stalks and 5 rows of potatoes, how many crops does the farmer still have?"""
    corn_rows = 10
    potato_rows = 5
    total_corn_cobs = corn_rows * 9
    total_potatoes = potato_rows * 30
    total_crops = total_corn_cobs + total_potatoes
    remaining_crops = total_crops * 0.5
    result = remaining_crops
    return result

print(solution())