def solution():
    
    birds_on_day_one = 300
    birds_on_day_two = birds_on_day_one * 2
    birds_on_day_three = birds_on_day_two - 200
    total_birds = birds_on_day_one + birds_on_day_two + birds_on_day_three
    result = total_birds
    return result

print(solution())