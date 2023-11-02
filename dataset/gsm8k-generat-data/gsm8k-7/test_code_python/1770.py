def solution():
    intro_length = 450
    conclusion_length = intro_length * 3
    total_length = 5000
    body_sections = 4

    # Calculate the total length of the introduction and conclusion
    intro_conclusion_length = intro_length + conclusion_length

    # Calculate the total length of the body sections
    body_length = (total_length - intro_conclusion_length) / body_sections

    result = body_length
    return result

print(solution())