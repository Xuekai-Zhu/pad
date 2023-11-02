def solution():
    original_price = 500
    reduced_price = original_price * 0.95  # 5% reduction
    further_reduced_price = reduced_price * 0.96  # 4% reduction a month after

    total_reduction = original_price - further_reduced_price
    result = total_reduction
    return result

print(solution())