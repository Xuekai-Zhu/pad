def solution():
    rachel_age = 12  # Rachel is 12 years old
    grandfather_age = 7 * rachel_age  # Grandfather is 7 times Rachel's age
    mother_age = 0.5 * grandfather_age  # Mother is half grandfather's age
    father_age = mother_age + 5  # Father is 5 years older than mother

    years_passed = 25 - rachel_age  # Years passed when Rachel is 25
    father_age_in_future = father_age + years_passed  # Father's age when Rachel is 25

    result = father_age_in_future
    return result

print(solution())