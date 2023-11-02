def solution():
    
    total_reviews = 18
    total_stars = (6 * 5) + (7 * 4) + (4 * 3) + (1 * 2)
    average_rating = total_stars / total_reviews
    result = average_rating
    return result

print(solution())