def solution():
    percent_rounded_up = 90
    total_sheep = 81
    sheep_rounded_up = total_sheep * (percent_rounded_up / 100)
    sheep_remaining = total_sheep - sheep_rounded_up
    result = sheep_remaining
    return result

print(solution())