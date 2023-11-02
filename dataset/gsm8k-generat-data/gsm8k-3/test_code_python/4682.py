def solution():
    """The Indigo Restaurant receives 18 online customer reviews. They receive six 5-star reviews, seven 4-star reviews, four 3-star reviews, and one 2-star review. What is the average star rating for Indigo Restaurant based on these reviews?"""
    # Define the number of reviews for each star rating
    FIVE_STAR_REVIEWS = 6
    FOUR_STAR_REVIEWS = 7
    THREE_STAR_REVIEWS = 4
    TWO_STAR_REVIEWS = 1

    # Calculate the total number of stars
    total_stars = (FIVE_STAR_REVIEWS * 5) + (FOUR_STAR_REVIEWS * 4) + (THREE_STAR_REVIEWS * 3) + (TWO_STAR_REVIEWS * 2)

    # Calculate the average star rating
    average_rating = total_stars / 18

    # Display the average rating
    result = average_rating
    return result

print(solution())