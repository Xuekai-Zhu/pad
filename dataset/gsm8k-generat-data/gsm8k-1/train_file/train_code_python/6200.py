def solution():
    """Out of the 300 comic books in a comic store, 30% are liked by females, males like 120, and both genders don't like the rest. What percentage of the comic books are disliked by both males and females?"""
    total_books = 300
    female_likes = total_books * 0.3
    male_likes = 120
    both_likes = female_likes + male_likes
    dislikes = total_books - both_likes
    percent_dislikes = (dislikes / total_books) * 100
    result = percent_dislikes
    return result

print(solution())