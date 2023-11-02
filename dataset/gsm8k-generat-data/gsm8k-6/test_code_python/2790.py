def solution():
    # Calculate the total amount of fresh bamboo sprouts eaten by the 9 pandas in one day
    total_bamboo = 4*25 + 5*40  # 4 small pandas eat 25 pounds, 5 bigger pandas eat 40 pounds
    # Calculate the total amount of fresh bamboo sprouts eaten by the 9 pandas in a week
    total_bamboo_week = total_bamboo * 7  # 7 days in a week
    result = total_bamboo_week
    return result

print(solution())