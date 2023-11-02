def solution():
    """Calen originally had 5 more pencils than does Caleb, and Caleb has 3 less than twice as many pencils as does Candy. 
    If Calen lost 10 pencils, which left him with 10 pencils, then how many pencils does Candy have?"""
    calen_start = 15 # Calen lost 10 pencils, so he started with 10 + 10 = 20
    caleb_start = calen_start - 5 # Calen originally had 5 more pencils than Caleb
    candy_start = (caleb_start + 3) / 2 # Caleb has 3 less than twice as many pencils as Candy
    return candy_start

# The answer should be 9.

print(solution())