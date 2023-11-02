def solution():
    """At a cafe, the breakfast plate has two eggs and twice as many bacon strips as eggs. If 14 customers order breakfast plates, how many bacon strips does the cook need to fry?"""
    # Define the number of eggs per breakfast plate
    eggs_per_plate = 2

    # Define the number of bacon strips per egg
    bacon_per_egg = 2

    # Calculate the total number of bacon strips needed
    total_bacon = eggs_per_plate * bacon_per_egg * 14

    # return the result
    result = total_bacon
    return result

print(solution())