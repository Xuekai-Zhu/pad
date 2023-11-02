def solution():
    # Calculate the total number of peppers picked
    total_peppers = 7 + 12 + 14 + 12 + 5 + 18 + 12

    # Calculate the number of hot peppers as 20% of the total number of peppers
    hot_peppers = total_peppers * 0.2

    # Calculate the number of non-hot peppers as the difference between the total number of peppers and the number of hot peppers
    non_hot_peppers = total_peppers - hot_peppers
    result = non_hot_peppers
    return result

print(solution())