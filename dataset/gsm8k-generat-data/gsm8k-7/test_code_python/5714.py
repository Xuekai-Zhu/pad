def solution():
    peppers_per_slice = 1/8
    peppers_per_sandwich = 4
    sandwiches_per_hour = 60/5  # 12
    sandwiches_per_day = sandwiches_per_hour * 8  # 96

    # Calculate the total number of jalapeno peppers needed for all sandwiches
    total_peppers = peppers_per_sandwich * sandwiches_per_day
    result = total_peppers
    return result

print(solution())