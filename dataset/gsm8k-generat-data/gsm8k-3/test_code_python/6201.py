def solution():
    """Out of the 300 comic books in a comic store, 30% are liked by females, males like 120, and both genders don't like the rest. What percentage of the comic books are disliked by both males and females?"""
    # Define the total number of comic books and the number liked by females
    total_comics = 300
    fem_liked = int(total_comics * 0.3)

    # Calculate the number of comics liked by males
    male_liked = 120

    # Calculate the number of comics disliked by both males and females
    disliked = total_comics - fem_liked - male_liked

    # Calculate the percentage of comics disliked by both males and females
    percent_disliked = int((disliked / total_comics) * 100)

    # Display the result
    result = percent_disliked
    return result

print(solution())