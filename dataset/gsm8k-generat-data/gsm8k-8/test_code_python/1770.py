def solution():
    # Define the length of the introduction
    intro_length = 450

    # Calculate the length of the conclusion
    conclusion_length = intro_length * 3

    # Calculate the total length of the body sections
    body_length = 5000 - (intro_length + conclusion_length)

    # Divide the total length of the body sections evenly among the four sections
    section_length = body_length / 4

    result = section_length
    return result

print(solution())