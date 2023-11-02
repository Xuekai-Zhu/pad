def solution():
    intro_length = 450  # introduction length is 450 words
    conclusion_length = intro_length * 3  # conclusion length is triple that of the introduction
    body_sections = 4  # there are four body sections
    total_words = 5000  # the essay has to be 5000 words in all

    # calculate the total length of the body sections
    body_length = total_words - intro_length - conclusion_length 

    # divide the total length of the body sections equally among the four sections
    section_length = body_length / body_sections
    result = section_length
    return result

print(solution())