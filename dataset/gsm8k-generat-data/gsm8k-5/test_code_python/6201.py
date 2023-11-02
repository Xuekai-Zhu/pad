def solution():
    total_comics = 300
    male_likes = 120
    female_likes = int(total_comics * 0.30)
    both_likes = male_likes - female_likes

    # Calculate the total number of comics disliked by both male and female
    both_dislikes = total_comics - (male_likes + female_likes + both_likes)

    # Calculate the percentage of comics disliked by both male and female
    percentage_dislikes = (both_dislikes / total_comics) * 100
    result = percentage_dislikes
    return result

print(solution())