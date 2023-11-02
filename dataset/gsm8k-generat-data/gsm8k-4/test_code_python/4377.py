def solution():
    """Calen originally had 5 more pencils than does Caleb, and Caleb has 3 less than twice as many pencils as does Candy. 
    If Calen lost 10 pencils, which left him with 10 pencils, then how many pencils does Candy have?"""
    
    # Calculate the original number of pencils Calen had
    calen_original = 20

    # Calculate the original number of pencils Caleb had
    caleb_original = (calen_original - 5) / 2

    # Calculate the original number of pencils Candy had
    candy_original = (caleb_original + 3) / 2

    # Calculate the current number of pencils Candy has
    candy_current = candy_original + 10

    # Return the result
    result = candy_current
    return result

print(solution())