def solution():
    father_age = 50 + 24  # Harry's father is currently 24 years older than he is
    mother_age_difference = 50 / 25  # Harry's mother is younger than his father by 1/25 of his current age
    mother_age = father_age - mother_age_difference  # Calculate Harry's mother's age when he was born
    age_when_gave_birth = mother_age - (50 / 2)  # Calculate how old Harry's mother was when she gave birth to him
    result = age_when_gave_birth
    return result

print(solution())