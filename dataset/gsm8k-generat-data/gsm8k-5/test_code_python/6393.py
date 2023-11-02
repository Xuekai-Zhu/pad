def solution():
    total_items = 18 + 12 + 17 + 13  # Find the total number of clothes to be washed
    cycles = total_items // 15 + 1  # Find the total number of cycles needed, accounting for any remaining items
    wash_time = cycles * 0.75  # Calculate the total time needed to wash all clothes in hours, each cycle takes 45 minutes or 0.75 hours

    result = wash_time
    return result

print(solution())