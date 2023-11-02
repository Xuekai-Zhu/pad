def solution():
    # Calculate the total number of stars received by the restaurant
    total_stars = 5*6 + 4*7 + 3*4 + 2*1  # six 5-star reviews, seven 4-star reviews, four 3-star reviews, and one 2-star review

    # Calculate the average star rating
    average_rating = total_stars / 18

    result = average_rating
    return result

print(solution())