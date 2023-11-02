def solution():
    """The bakery makes 3 batches of baguettes a day. Each batch has 48 baguettes. After the first batch came out, he sold 37. After the second batch, he sold 52. After the third batch he sold 49. How many baguettes are left?"""
    batches_per_day = 3
    baguettes_per_batch = 48
    sold_in_first_batch = 37
    sold_in_second_batch = 52
    sold_in_third_batch = 49
    total_baked = batches_per_day * baguettes_per_batch
    total_sold = sold_in_first_batch + sold_in_second_batch + sold_in_third_batch
    left_over = total_baked - total_sold
    result = left_over
    return result

print(solution())