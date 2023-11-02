def solution():
    # Calculate the age of Rachel's grandfather
    grandfather_age = 7 * 12  # Rachel's grandfather is 7 times her age

    # Calculate the age of Rachel's mother
    mother_age = grandfather_age / 2  # her mother is half her grandfather's age

    # Calculate the age of Rachel's father
    father_age = mother_age + 5  # her father is 5 years older than her mother

    # Calculate how many years from now Rachel will be 25
    years_from_now = 25 - 12  # Rachel is currently 12 years old

    # Calculate how old Rachel's father will be when she is 25
    father_age_at_25 = father_age + years_from_now
    result = father_age_at_25
    return result

print(solution())