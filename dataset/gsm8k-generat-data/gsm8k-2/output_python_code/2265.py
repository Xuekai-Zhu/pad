def solution():
    """Haley has 5 more necklaces than Jason. Josh has half the number of necklaces as Jason. If Haley has 25 necklaces, how many more necklaces does Haley have than Josh?"""
    haley_necklaces = 25
    jason_necklaces = haley_necklaces - 5
    josh_necklaces = jason_necklaces / 2
    difference = haley_necklaces - josh_necklaces
    result = difference
    return result

print(solution())