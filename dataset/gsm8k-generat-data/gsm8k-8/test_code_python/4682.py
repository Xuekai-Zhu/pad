def solution():
    # Calculate the total number of stars received
    total_stars = 5*6 + 4*7 + 3*4 + 2*1

    # Calculate the total number of reviews
    total_reviews = 6 + 7 + 4 + 1

    # Calculate the average star rating
    average_rating = total_stars / total_reviews
    result = average_rating
    return result

print(solution())