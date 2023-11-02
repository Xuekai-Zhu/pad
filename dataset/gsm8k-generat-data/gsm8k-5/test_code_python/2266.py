def solution():
    haley_necklaces = 25  # Haley has 25 necklaces
    jason_necklaces = haley_necklaces - 5  # Jason has 5 fewer necklaces than Haley
    josh_necklaces = jason_necklaces / 2  # Josh has half the number of necklaces as Jason

    # Calculate the difference between Haley and Josh's necklaces
    difference = haley_necklaces - josh_necklaces
    result = difference
    return result

print(solution())