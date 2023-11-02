def solution():
    """Nadine's dog rolls around in the mud. She spends 10 minutes hosing him off outside, then shampoos him three times, which takes 15 minutes per shampoo. How long does she spend cleaning her dog total?"""
    hosing_time = 10
    shampoo_time = 15
    num_shampoos = 3
    total_shampoo_time = shampoo_time * num_shampoos
    total_cleaning_time = hosing_time + total_shampoo_time
    result = total_cleaning_time
    return result

print(solution())