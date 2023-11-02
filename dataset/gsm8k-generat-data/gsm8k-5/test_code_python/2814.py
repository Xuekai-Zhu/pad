def solution():
    total_time = 90  # Josie's shopping trip took an hour and a half
    waiting_time = 3 + 13 + 14 + 18  # Josie spent a total of 48 minutes waiting
    shopping_time = total_time - waiting_time  # Josie spent the remaining time shopping
    result = shopping_time
    return result

print(solution())