def solution():
    """Martha's cat catches 3 rats and 7 birds. Cara's cat catches 3 less than five times as many animals as Martha's cat. How many animals does Cara's cat catch?"""
    martha_total = 3 + 7
    cara_total = (5 * martha_total) - 3
    result = cara_total
    return result

print(solution())