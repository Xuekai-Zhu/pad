def solution():
    original_length = 30  # seconds
    reduction_percentage = 0.3  # 30% reduction
    new_length = original_length - (original_length * reduction_percentage)
    result = new_length
    return result

print(solution())