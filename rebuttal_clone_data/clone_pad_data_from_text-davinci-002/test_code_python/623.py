def solution():
    iced_tea_cups = 1/4
    lemonade_cups = 1 + 1/4
    total_cups = 18
    lemonade_cups_in_pitcher = total_cups * (lemonade_cups / (iced_tea_cups + lemonade_cups))
    result = lemonade_cups_in_pitcher
    return result

print(solution())