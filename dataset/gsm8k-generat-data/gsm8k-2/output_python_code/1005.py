def solution():
    """When Jayson is 10 his dad is four times his age and his mom is 2 years younger than his dad. How old was Jayson's mom when he was born?"""
    jayson_age = 10
    dad_age = 4 * jayson_age
    mom_age = dad_age - 2
    mom_age_when_jayson_was_born = mom_age - jayson_age
    result = mom_age_when_jayson_was_born
    return result

print(solution())