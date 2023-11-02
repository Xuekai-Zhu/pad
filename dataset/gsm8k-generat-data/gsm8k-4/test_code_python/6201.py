def solution():
    """Out of the 300 comic books in a comic store, 30% are liked by females, males like 120, and both genders don't like the rest. What percentage of the comic books are disliked by both males and females?"""
    # Define the total number of comic books
    total_comics = 300

    # Calculate the number of comic books liked by females
    comics_liked_by_females = total_comics * 0.3

    # Calculate the number of comic books liked by males
    comics_liked_by_males = 120

    # Calculate the number of comic books disliked by both males and females
    comics_disliked_by_both = total_comics - comics_liked_by_females - comics_liked_by_males

    # Calculate the percentage of comic books disliked by both males and females
    percentage_disliked = (comics_disliked_by_both / total_comics) * 100

    # Return the result
    result = percentage_disliked
    return result

print(solution())