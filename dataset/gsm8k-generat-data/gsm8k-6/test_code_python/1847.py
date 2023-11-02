def solution():
    # Find the total number of bottles Martha had after buying more juice
    total_bottles = 4 + 4 + 5  # 4 bottles in the refrigerator, 4 bottles in the pantry, and 5 more bought
    # Calculate the number of bottles left after Martha and her family drank 3 bottles
    bottles_left = total_bottles - 3
    result = bottles_left
    return result

print(solution())