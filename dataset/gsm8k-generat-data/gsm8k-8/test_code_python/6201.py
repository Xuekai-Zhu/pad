def solution():
    # Define the total number of comic books and the number liked by females
    total_books = 300
    female_likes = 0.3 * total_books

    # Calculate the number of books liked by males only
    male_likes = 120
    male_only_likes = male_likes - (male_likes * 0.3)

    # Calculate the number of books disliked by both genders
    neither_likes = total_books - (female_likes + male_only_likes + male_likes)

    # Calculate the percentage of books disliked by both genders
    percentage_disliked = (neither_likes / total_books) * 100
    result = percentage_disliked
    return result

print(solution())