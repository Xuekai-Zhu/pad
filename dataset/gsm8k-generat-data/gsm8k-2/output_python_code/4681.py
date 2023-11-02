def solution():
    """The Indigo Restaurant receives 18 online customer reviews. They receive six 5-star reviews, seven 4-star reviews, four 3-star reviews, and one 2-star review. What is the average star rating for Indigo Restaurant based on these reviews?"""
    total_stars = (6 * 5) + (7 * 4) + (4 * 3) + (1 * 2)
    num_reviews = 18
    avg_rating = total_stars / num_reviews
    result = avg_rating
    return result

print(solution())