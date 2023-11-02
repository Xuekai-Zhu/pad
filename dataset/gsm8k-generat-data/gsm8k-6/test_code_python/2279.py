def solution():
    # Calculate the total number of shoes Austin needs to polish
    total_shoes = 10 * 2  # 10 pairs of shoes, with 2 shoes in each pair
    polished_shoes = total_shoes * 0.45  # 45% of shoes already polished
    shoes_left = total_shoes - polished_shoes  # calculate the number of shoes left to polish
    result = shoes_left
    return result

print(solution())