def solution():
    
    seashells_collected = 180
    seashells_given_away = 40 + 30
    seashells_left = seashells_collected - seashells_given_away
    seashells_sold = seashells_left / 2
    seashells_remaining = seashells_left - seashells_sold
    result = seashells_remaining
    return result

print(solution())