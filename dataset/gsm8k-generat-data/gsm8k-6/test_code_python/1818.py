def solution():
    # Calculate the total number of peppers picked
    total_peppers = 7 + 12 + 14 + 12 + 5 + 18 + 12
    hot_peppers = total_peppers * 0.2  # 20% of the peppers are hot
    non_hot_peppers = total_peppers - hot_peppers  # the rest are not hot
    result = non_hot_peppers
    return result

print(solution())