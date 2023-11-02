def solution():
    """Calen originally had 5 more pencils than does Caleb, and Caleb has 3 less than twice as many pencils as does Candy.  If Calen lost 10 pencils, which left him with 10 pencils, then how many pencils does Candy have?"""
    # Let x be the number of pencils Candy has
    x = 0

    # Caleb has 3 less than twice as many as Candy
    caleb_pencils = 2*x - 3

    # Calen originally had 5 more pencils than Caleb
    calen_pencils = caleb_pencils + 5

    # Calen lost 10 pencils, leaving him with 10
    calen_pencils -= 10

    # Solve for x
    x = (calen_pencils - 5 + 3) / 2

    # Display the number of pencils Candy has
    result = x
    return result

print(solution())