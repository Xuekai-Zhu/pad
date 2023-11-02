def solution():
    total_comic_books = 300
    males_like = 120
    females_like_percentage = 0.3

    # Calculate the number of comic books liked by females
    females_like = total_comic_books * females_like_percentage

    # Calculate the number of comic books disliked by both genders
    both_dislike = total_comic_books - males_like - females_like

    # Calculate the percentage of comic books disliked by both genders
    percentage_both_dislike = (both_dislike / total_comic_books) * 100
    result = percentage_both_dislike
    return result

print(solution())