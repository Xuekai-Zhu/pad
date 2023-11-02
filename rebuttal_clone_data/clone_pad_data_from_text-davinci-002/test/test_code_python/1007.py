def solution():
    intro_length = 450
    conclusion_length = intro_length * 3
    body_length = (5000 - intro_length - conclusion_length) / 4
    result = body_length
    return result

print(solution())