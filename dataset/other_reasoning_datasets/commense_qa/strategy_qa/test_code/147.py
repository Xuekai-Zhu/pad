def solution():
    steven_birth_year = 1946
    email_public_availability_year = 1995
    if steven_birth_year < email_public_availability_year:
        result = "no"
    else:
        result = "yes"
    return result

print(solution())