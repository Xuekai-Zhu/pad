def solution():
    """The Indigo Restaurant receives 18 online customer reviews. They receive six 5-star reviews, seven 4-star reviews, four 3-star reviews, and one 2-star review. What is the average star rating for Indigo Restaurant based on these reviews?"""
    # Define the number of each star rating
    five_star = 6
    four_star = 7
    three_star = 4
    two_star = 1

    # Calculate the sum of all star ratings
    star_sum = (5 * five_star) + (4 * four_star) + (3 * three_star) + (2 * two_star)

    # Calculate the total number of reviews
    total_reviews = five_star + four_star + three_star + two_star

    # Calculate the average star rating
    average_rating = star_sum / total_reviews

    result = average_rating
    return result

print(solution())