def solution():
    total_spent = 120
    spent_on_saturday = 2 * x
    spent_on_sunday = 3 * x
    x = (total_spent - spent_on_saturday - spent_on_sunday) / 6
    return x

print(solution())