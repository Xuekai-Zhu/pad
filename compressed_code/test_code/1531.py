def solution():
    
    total_boats = 30
    fish_eaten = 0.2 * total_boats
    remaining_boats = total_boats - fish_eaten - 2
    result = remaining_boats
    return result

print(solution())