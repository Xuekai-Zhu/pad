def solution():
    """The bakery makes 3 batches of baguettes a day. Each batch has 48 baguettes. After the first batch came out, he sold 37. After the second batch, he sold 52. After the third batch he sold 49. How many baguettes are left?"""
    # Define the number of batches and baguettes per batch
    BATCHES_PER_DAY = 3
    BAGUETTES_PER_BATCH = 48

    # Calculate the total number of baguettes made
    total_baguettes = BATCHES_PER_DAY * BAGUETTES_PER_BATCH

    # Calculate the number of baguettes sold
    sold_baguettes = 37 + 52 + 49

    # Calculate the number of baguettes left
    remaining_baguettes = total_baguettes - sold_baguettes

    # return the result
    result = remaining_baguettes
    return result

print(solution())