def solution():
    peppers_picked = [7, 12, 14, 12, 5, 18, 12]
    hot_percentage = 0.2  # 20% are hot
    total_peppers = sum(peppers_picked)

    # Calculate the number of hot peppers picked
    num_hot_peppers = total_peppers * hot_percentage

    # Calculate the number of non-hot peppers picked
    num_non_hot_peppers = total_peppers - num_hot_peppers
    result = num_non_hot_peppers
    return result

print(solution())