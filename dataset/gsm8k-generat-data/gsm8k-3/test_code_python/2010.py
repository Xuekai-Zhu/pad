def solution():
    """Stan can type 50 words per minute. He needs to write a 5-page paper. Each page will contain 400 words. Each hour that he types he needs to drink 15 ounces of water. How much water does he need to drink while writing his paper?"""
    # Define the number of words per page and pages in the paper
    WORDS_PER_PAGE = 400
    PAGES = 5

    # Calculate the total number of words in the paper
    total_words = WORDS_PER_PAGE * PAGES

    # Calculate the time it will take to type the paper in minutes
    typing_time_minutes = total_words / 50

    # Calculate the total amount of water needed to be consumed
    water_needed = (typing_time_minutes / 60) * 15

    # Display the total amount of water needed
    result = water_needed
    return result

print(solution())