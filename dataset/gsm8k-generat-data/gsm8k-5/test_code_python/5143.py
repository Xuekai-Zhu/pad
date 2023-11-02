def solution():
    billy_age = 4  # Billy's current age is 4 years old
    my_age = 4 * billy_age  # I'm 4 times older than Billy currently

    # Calculate the age gap between me and Billy
    age_gap = my_age - billy_age

    # Subtract the age gap from my current age to find my age when Billy was born
    my_age_when_billy_was_born = my_age - age_gap
    result = my_age_when_billy_was_born
    return result

print(solution())