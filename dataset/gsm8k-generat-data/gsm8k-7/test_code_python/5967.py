def solution():
    first_week = 12
    second_week = first_week + 4
    third_week = (first_week + second_week) / 2
    fourth_week = third_week - 3
    total_socks = 4 + first_week + second_week + third_week + fourth_week
    result = total_socks
    return result

print(solution())