def solution():
    """A local park has 70 pigeons that call the park home. Half of the pigeons are black, and 20 percent of the black pigeons are male.  How many more black female pigeons are there than black male pigeons?"""
    # Define the total number of pigeons and the number of black pigeons
    total_pigeons = 70
    black_pigeons = total_pigeons / 2

    # Calculate the number of black male pigeons and black female pigeons
    black_male = black_pigeons * 0.2
    black_female = black_pigeons - black_male

    # Calculate the difference between black female pigeons and black male pigeons
    difference = black_female - black_male

    # return the result
    result = difference
    return result

print(solution())