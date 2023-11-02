def solution():
    """Out of the 300 comic books in a comic store, 30% are liked by females, males like 120, and both genders don't like the rest. What percentage of the comic books are disliked by both males and females?"""
    total_comics = 300
    female_liked = 0.3 * total_comics
    male_liked = 120
    both_liked = female_liked + male_liked
    disliked_by_both = total_comics - both_liked
    percent_disliked = (disliked_by_both / total_comics) * 100
    result = percent_disliked
    return result

print(solution())