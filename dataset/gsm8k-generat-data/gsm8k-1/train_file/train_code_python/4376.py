def solution():
    """Calen originally had 5 more pencils than does Caleb, and Caleb has 3 less than twice as many pencils as does Candy. If Calen lost 10 pencils, which left him with 10 pencils, then how many pencils does Candy have?"""
    calen_original = 15
    caleb_original = 10
    candy_original = (caleb_original + 3) / 2
    calen_current = 10
    calen_lost = calen_original - calen_current
    total_pencils = calen_current + caleb_original + candy_original
    candy_current = total_pencils - calen_current - caleb_original
    result = candy_current
    return result

print(solution())