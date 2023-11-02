def solution():
    """Stan can type 50 words per minute. He needs to write a 5-page paper. Each page will contain 400 words. Each hour that he types he needs to drink 15 ounces of water. How much water does he need to drink while writing his paper?"""
    # Define the number of words per page and the total number of pages
    WORDS_PER_PAGE = 400
    TOTAL_PAGES = 5

    # Calculate the total number of words
    total_words = WORDS_PER_PAGE * TOTAL_PAGES

    # Calculate the total time Stan will spend typing in minutes
    typing_time = total_words / 50

    # Calculate the number of hours Stan will spend typing
    typing_hours = typing_time / 60

    # Calculate the amount of water Stan needs to drink in ounces
    water_amount = typing_hours * 15

    # Return the result
    result = water_amount
    return result

print(solution())