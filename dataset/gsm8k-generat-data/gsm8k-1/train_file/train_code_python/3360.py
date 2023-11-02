def solution():
    """Agnes is 25 years old and her daughter, Jane is 6 years old. In how many years will Agnes be twice as old as Jane?"""
    agnes_age = 25
    jane_age = 6
    age_difference = agnes_age - jane_age
    years_until_double = age_difference
    while agnes_age != 2 * jane_age:
        agnes_age += 1
        jane_age += 1
        years_until_double += 1
    result = years_until_double
    return result

print(solution())