def solution():
    nominee_birth_year = 1860 #Assuming William Jennings Bryan was 48 years old when he ran for president in 1908
    tv_invention_year = 1927
    if nominee_birth_year < tv_invention_year:
        result = "no"
    else:
        result = "yes"
    return result

print(solution())