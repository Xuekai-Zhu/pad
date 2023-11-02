def solution():
    money_given = 100
    sharpeners = 2
    notebooks = 4
    erasers = 10
    total_spent = (sharpeners * 5) + (notebooks * 5) + (erasers * 4)
    money_left = money_given - total_spent
    highlighters = money_left / 4
    result = highlighters
    return result

print(solution())