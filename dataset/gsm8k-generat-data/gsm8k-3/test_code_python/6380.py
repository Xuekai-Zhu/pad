def solution():
    """A local park has 70 pigeons that call the park home. Half of the pigeons are black, and 20 percent of the black pigeons are male.  How many more black female pigeons are there than black male pigeons?"""
    # Calculate the number of black pigeons
    black_pigeons = 70 / 2

    # Calculate the number of black male pigeons
    black_male_pigeons = black_pigeons * 0.2

    # Calculate the number of black female pigeons
    black_female_pigeons = black_pigeons - black_male_pigeons

    # Calculate the difference between the number of black female and black male pigeons
    difference = black_female_pigeons - black_male_pigeons

    # Display the difference
    result = difference
    return result

print(solution())