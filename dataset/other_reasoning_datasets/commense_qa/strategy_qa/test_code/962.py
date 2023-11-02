def solution():
    impeachment_year = 1998
    end_of_term_year = 2001
    if impeachment_year < end_of_term_year:
        result = "no"
    else:
        result = "yes"
    return result

print(solution())