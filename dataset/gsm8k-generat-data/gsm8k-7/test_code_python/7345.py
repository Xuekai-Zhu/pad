def solution():
    birds_caught_during_day = 8
    birds_caught_at_night = birds_caught_during_day * 2
    
    # Calculate the total number of birds caught by the cat
    total_birds_caught = birds_caught_during_day + birds_caught_at_night
    result = total_birds_caught
    return result

print(solution())