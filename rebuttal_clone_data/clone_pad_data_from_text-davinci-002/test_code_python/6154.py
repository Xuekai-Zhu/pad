def solution():
    total_characters = 60
    a_characters = total_characters / 2
    c_characters = a_characters / 2
    d_characters = (total_characters - (a_characters + c_characters)) / 2
    e_characters = d_characters / 2
    result = d_characters
    return result

print(solution())