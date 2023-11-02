def solution():
    
    total_distance = 5000
    popcorn_per_distance = 1/25
    total_popcorn = total_distance * popcorn_per_distance
    eaten_popcorn = total_popcorn / 4
    remaining_popcorn = total_popcorn - eaten_popcorn
    result = remaining_popcorn
    return result

print(solution())