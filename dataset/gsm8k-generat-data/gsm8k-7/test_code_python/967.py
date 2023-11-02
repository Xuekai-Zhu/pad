def solution():
    current_temp = 84
    decrease_ratio = 3/4

    # Calculate the amount of temperature decrease
    temp_decrease = current_temp - (current_temp * decrease_ratio)

    result = temp_decrease
    return result

print(solution())