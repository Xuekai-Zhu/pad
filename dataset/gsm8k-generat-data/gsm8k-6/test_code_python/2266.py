def solution():
    haley_necklaces = 25  # given that Haley has 25 necklaces
    jason_necklaces = haley_necklaces - 5  # given that Haley has 5 more necklaces than Jason
    josh_necklaces = jason_necklaces / 2  # given that Josh has half the number of necklaces as Jason
    difference = haley_necklaces - josh_necklaces  # find the difference in number of necklaces between Haley and Josh
    result = difference
    return result

print(solution())