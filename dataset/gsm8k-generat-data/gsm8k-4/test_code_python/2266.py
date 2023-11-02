def solution():
    """Haley has 5 more necklaces than Jason. Josh has half the number of necklaces as Jason. If Haley has 25 necklaces, how many more necklaces does Haley have than Josh?"""
    # Define the number of necklaces Haley has
    haley_necklaces = 25

    # Calculate the number of necklaces Jason has
    jason_necklaces = haley_necklaces - 5

    # Calculate the number of necklaces Josh has
    josh_necklaces = jason_necklaces / 2

    # Calculate the difference between the number of necklaces Haley and Josh have
    difference = haley_necklaces - josh_necklaces

    result = difference
    return result

print(solution())