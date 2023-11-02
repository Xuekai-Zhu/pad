def solution():
    """Dana has 15 more pencils than Jayden, who has twice as much as Marcus. How many more pencils does Dana have than Marcus, if Jayden has 20 pencils?"""
    jayden_pencils = 20
    marcus_pencils = jayden_pencils / 2
    dana_pencils = jayden_pencils + 15
    difference = dana_pencils - marcus_pencils
    result = difference
    return result

print(solution())