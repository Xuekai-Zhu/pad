def solution():
    total_apples = 200  # total number of apples
    day1_picked = total_apples * (1/5)  # number of apples picked on the first day
    day2_picked = day1_picked * 2  # number of apples picked on the second day
    day3_picked = day1_picked + 20  # number of apples picked on the third day
    total_picked = day1_picked + day2_picked + day3_picked  # total number of apples picked
    remaining_apples = total_apples - total_picked  # number of apples remaining on the tree

    result = remaining_apples
    return result

print(solution())