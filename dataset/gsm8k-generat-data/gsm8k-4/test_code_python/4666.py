def solution():
    """Dana has 15 more pencils than Jayden, who has twice as much as Marcus. How many more pencils does Dana have than Marcus, if Jayden has 20 pencils?"""
    # Define the number of pencils Jayden has
    jayden_pencils = 20

    # Calculate the number of pencils Marcus has
    marcus_pencils = jayden_pencils / 2

    # Calculate the number of pencils Dana has
    dana_pencils = jayden_pencils + 15

    # Calculate the difference between Dana's and Marcus's pencils
    difference = dana_pencils - marcus_pencils

    # return the result
    result = difference
    return result

print(solution())