def solution():
    num_shoes = 10
    percent_polished = 0.45  # 45%

    # Calculate the number of shoes already polished
    num_polished = round(num_shoes * percent_polished)

    # Calculate the number of shoes left to polish
    num_left_to_polish = num_shoes - num_polished
    result = num_left_to_polish
    return result

print(solution())