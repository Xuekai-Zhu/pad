def solution():
    num_five_star = 6
    num_four_star = 7
    num_three_star = 4
    num_two_star = 1
    num_total_reviews = num_five_star + num_four_star + num_three_star + num_two_star

    # Calculate the total number of stars
    total_stars = (num_five_star * 5) + (num_four_star * 4) + (num_three_star * 3) + (num_two_star * 2)

    # Calculate the average star rating
    average_rating = total_stars / num_total_reviews
    result = average_rating
    return result

print(solution())