def solution():
    batches_per_day = 3  # The bakery makes 3 batches of baguettes a day
    baguettes_per_batch = 48  # Each batch has 48 baguettes

    # Calculate the total number of baguettes made in a day
    total_baguettes = batches_per_day * baguettes_per_batch

    # Calculate the number of baguettes sold
    baguettes_sold = 37 + 52 + 49

    # Calculate the number of baguettes left
    baguettes_left = total_baguettes - baguettes_sold
    result = baguettes_left
    return result

print(solution())