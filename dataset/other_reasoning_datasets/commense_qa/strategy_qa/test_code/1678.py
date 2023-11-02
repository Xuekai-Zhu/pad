def solution():
    helen_keller_death_year = 1968
    jk_rowling_first_novel_year = 1997
    if helen_keller_death_year < jk_rowling_first_novel_year:
        result = "no"
    else:
        result = "unclear"
    return result

print(solution())