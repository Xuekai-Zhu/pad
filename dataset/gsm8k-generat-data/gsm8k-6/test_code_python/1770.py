def solution():
    # Calculate the length of each body section
    intro = 450
    conclusion = intro * 3
    body_total = 5000 - intro - conclusion
    body_section_length = body_total / 4
    result = body_section_length
    return result

print(solution())