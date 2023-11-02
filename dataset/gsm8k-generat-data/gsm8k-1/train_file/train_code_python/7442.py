def solution():
    """Harry is 50 years old. His father is currently 24 years older than he is. How old was his mother when she gave birth to him if she is younger than his father by 1/25 of Harry's current age?"""
    harry_age = 50
    father_age = harry_age + 24
    mother_age = father_age - harry_age/25 - harry_age
    mother_birth_age = mother_age - harry_age
    result = mother_birth_age
    return result

print(solution())