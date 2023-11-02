def solution():
    # Calculate the number of comic books liked by females
    liked_by_females = int(0.3 * 300)

    # Calculate the number of comic books liked by males only
    liked_by_males_only = 120 - liked_by_females

    # Calculate the number of comic books disliked by both males and females
    disliked_by_both = 300 - (liked_by_females + liked_by_males_only)

    # Calculate the percentage of comic books disliked by both males and females
    percentage_disliked = (disliked_by_both / 300) * 100
    result = percentage_disliked
    return result

print(solution())