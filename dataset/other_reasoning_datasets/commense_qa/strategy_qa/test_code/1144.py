def solution():
    great_depression_start = 1929
    great_depression_end = 1933
    harry_potter_publication_year = 1997
    if harry_potter_publication_year > great_depression_end:
        result = "yes"
    else:
        result = "no"
    return result

print(solution())