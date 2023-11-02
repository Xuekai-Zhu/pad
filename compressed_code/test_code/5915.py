def solution():
    
    bottles_with_stars = 2
    star_capacity = 15
    total_stars = bottles_with_stars * star_capacity
    remaining_bottles = 3
    total_bottles = bottles_with_stars + remaining_bottles
    stars_needed = total_bottles * star_capacity
    result = stars_needed
    return result

print(solution())