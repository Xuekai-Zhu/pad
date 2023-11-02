def solution():
    total_kids = 20
    kids_asleep_1 = total_kids / 2
    kids_asleep_2 = kids_asleep_1 / 2
    kids_awake = total_kids - (kids_asleep_1 + kids_asleep_2)
    result = kids_awake
    return result

print(solution())