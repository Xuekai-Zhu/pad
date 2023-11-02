def solution():
    """The Indigo Restaurant receives 18 online customer reviews. They receive six 5-star reviews, seven 4-star reviews, four 3-star reviews, and one 2-star review.
    What is the average star rating for Indigo Restaurant based on these reviews?"""
    total_reviews = 18
    total_stars = (6 * 5) + (7 * 4) + (4 * 3) + (1 * 2)
    average_rating = total_stars / total_reviews
    result = average_rating
    return result

print(solution())