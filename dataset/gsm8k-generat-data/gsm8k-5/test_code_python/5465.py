def solution():
    original_price = 800  # The laptop originally costs $800
    reduction_rate = 0.15  # There is a 15% reduction in the price
    reduced_amount = original_price * reduction_rate  # Calculate the amount reduced
    final_price = original_price - reduced_amount  # Calculate the final price after the reduction
    result = final_price
    return result

print(solution())