def solution():
    """Joshua, Jose, and Albert are collecting rocks. Joshua collected 80 rocks while Jose collected 14 fewer rocks. Albert has collected 20 more rocks than Jose. How many more rocks did Albert collect than Joshua?"""
    # Define the number of rocks Joshua collected
    joshua_rocks = 80

    # Calculate the number of rocks Jose collected
    jose_rocks = joshua_rocks - 14

    # Calculate the number of rocks Albert collected
    albert_rocks = jose_rocks + 20

    # Calculate the difference between the number of rocks Albert and Joshua collected
    difference = albert_rocks - joshua_rocks

    # Display the difference
    result = difference
    return result

print(solution())