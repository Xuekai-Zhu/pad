def solution():
    # Calculate the height difference for each crane
    crane1_diff = (228 - 200) / 200
    crane2_diff = (120 - 100) / 100
    crane3_diff = (147 - 140) / 140

    # Calculate the average height difference as a percentage
    avg_diff_percent = ((crane1_diff + crane2_diff + crane3_diff) / 3) * 100
    result = avg_diff_percent
    return result

print(solution())