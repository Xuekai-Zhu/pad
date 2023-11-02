def solution():
    # Calculate the total number of chicken parts Steph has
    total_parts = 24 + (24-4)  # 24 drumsticks and 4 fewer breast parts (20 breast parts)
    # Calculate the total number of fried chickens Steph can make
    fried_chickens = total_parts // 2  # 2 parts (drumstick or breast) make 1 fried chicken
    result = fried_chickens
    return result

print(solution())