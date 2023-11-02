def solution():
    """Jaydee can type 38 words in a minute. How many hours will he take to finish typing a research paper with 4560 words?"""
    # Define the typing speed and the number of words in the research paper
    TYPING_SPEED = 38
    WORDS_IN_RESEARCH_PAPER = 4560

    # Calculate the number of minutes it will take to type the research paper
    minutes = WORDS_IN_RESEARCH_PAPER / TYPING_SPEED

    # Convert minutes to hours
    hours = minutes / 60

    # Display the number of hours it will take to type the research paper
    result = hours
    return result

print(solution())