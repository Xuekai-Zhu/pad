def solution():
    """Carolyn is planning out her final essay. The introduction will be 450 words, the conclusion will be triple the length of the introduction, and each of the four body sections will be the same length. If her essay has to be 5000 words total, how long is each section?"""
    # Define the length of the introduction
    introduction_length = 450

    # Define the length of the conclusion
    conclusion_length = 3 * introduction_length

    # Calculate the total length of the essay with the introduction and conclusion
    essay_length = introduction_length + conclusion_length

    # Calculate the remaining length for the body sections
    body_length = 5000 - essay_length

    # Calculate the length of each body section
    section_length = body_length / 4

    # Return the result
    result = section_length
    return result

print(solution())