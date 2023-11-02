def solution():
    """Joshua collected 80 rocks while Jose collected 14 fewer rocks.
    Albert has collected 20 more rocks than Jose. How many more rocks did Albert collect than Joshua?"""
    # Define the number of rocks collected by Joshua
    joshua_rocks = 80

    # Calculate the number of rocks collected by Jose
    jose_rocks = joshua_rocks - 14

    # Calculate the number of rocks collected by Albert
    albert_rocks = jose_rocks + 20

    # Calculate the difference between the number of rocks collected by Albert and Joshua
    difference = albert_rocks - joshua_rocks

    # return the result
    result = difference
    return result

print(solution())