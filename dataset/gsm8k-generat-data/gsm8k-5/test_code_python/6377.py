def solution():
    total_apples = 200  # The apple tree yielded 200 apples
    day1_picked = total_apples // 5  # Magdalena picked 1/5 of the apples on day 1
    day2_picked = day1_picked * 2  # Magdalena picked twice as many apples on day 2
    day3_picked = day1_picked + 20  # Magdalena picked 20 more apples on day 3
    total_picked = day1_picked + day2_picked + day3_picked  # Total number of apples picked

    # Calculate the number of apples remaining on the tree
    apples_remaining = total_apples - total_picked
    result = apples_remaining
    return result

print(solution())