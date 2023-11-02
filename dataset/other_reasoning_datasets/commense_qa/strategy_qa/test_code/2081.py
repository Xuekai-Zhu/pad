def solution():
    hamlet_author = "William Shakespeare"
    author_birth_year = 1564
    email_widespread_use_year = 1970
    if author_birth_year < email_widespread_use_year:
        result = "no"
    else:
        result = "yes"
    return result

print(solution())