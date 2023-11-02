def solution():
    """Carolyn is planning out her final essay. The introduction will be 450 words, the conclusion will be triple the length of the introduction, and each of the four body sections will be the same length. If her essay has to be 5000 words total, how long is each section?"""
    # Define the length of the introduction and the number of body sections
    intro_length = 450
    num_body_sections = 4

    # Calculate the length of the conclusion
    conclusion_length = intro_length * 3

    # Calculate the total length of the introduction, conclusion, and body sections
    total_body_length = 5000 - intro_length - conclusion_length
    body_section_length = total_body_length / num_body_sections

    # Display the length of each section
    result = body_section_length
    return result

print(solution())