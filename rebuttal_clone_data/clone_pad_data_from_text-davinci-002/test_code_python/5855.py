def solution():
    day_one = 1
    day_two = day_one / 2
    day_three = day_two / 2
    day_four = day_three / 2
    worms_left = 4
    worms_eaten = day_one + day_two + day_three + day_four
    worms_total = worms_eaten + worms_left
    result = worms_total
    return result

print(solution())