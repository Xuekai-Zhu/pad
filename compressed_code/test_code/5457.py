def solution():
    
    batch_size = 48
    total_batches = 3
    first_batch_sold = 37
    second_batch_sold = 52
    third_batch_sold = 49
    total_sold = first_batch_sold + second_batch_sold + third_batch_sold
    total_baguettes = batch_size * total_batches
    left_over_baguettes = total_baguettes - total_sold
    result = left_over_baguettes
    return result

print(solution())