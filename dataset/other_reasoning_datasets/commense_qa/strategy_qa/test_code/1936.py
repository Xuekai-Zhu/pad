def solution():
    average_temp_range = ("-4", "36")
    highest_temp_recorded = "50"
    unusual_temp = "75"
    if unusual_temp > max(average_temp_range) or unusual_temp > highest_temp_recorded:
        result = "yes"
    else:
        result = "no"
    return result

print(solution())