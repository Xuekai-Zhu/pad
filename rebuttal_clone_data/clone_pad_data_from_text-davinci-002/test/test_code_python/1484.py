def solution():
    birds_on_monday = 70
    birds_on_tuesday = birds_on_monday / 2
    birds_on_wednesday = birds_on_tuesday + 8
    total_birds = birds_on_monday + birds_on_tuesday + birds_on_wednesday
    result = total_birds
    return result

print(solution())