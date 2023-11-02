def solution():
    # Calculate the total number of roses and red roses
    total_roses = 10 * 20  # 10 rows of 20 roses
    red_roses = total_roses / 2  # half of the roses are red

    # Calculate the number of white roses and pink roses
    white_roses = (total_roses - red_roses) * 3 / 5  # 3/5 of the remaining roses are white
    pink_roses = total_roses - red_roses - white_roses  # the rest are pink

    result = pink_roses
    return result

print(solution())