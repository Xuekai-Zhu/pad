def solution():
    num_reviews = 18  # The Indigo Restaurant receives 18 online customer reviews
    num_5_stars = 6  # They receive six 5-star reviews
    num_4_stars = 7  # They receive seven 4-star reviews
    num_3_stars = 4  # They receive four 3-star reviews
    num_2_stars = 1  # They receive one 2-star review

    # Calculate the total number of stars received
    total_stars = (5 * num_5_stars) + (4 * num_4_stars) + (3 * num_3_stars) + (2 * num_2_stars)

    # Calculate the average star rating
    average_rating = total_stars / num_reviews
    result = average_rating
    return result

print(solution())