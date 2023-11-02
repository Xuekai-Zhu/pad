def solution():
    """Derek finally gets his own allowance. He puts $2 away in January, $4 away in February, $8 away in March, $16 away in April and follows this savings pattern through to December. How much money does he have to spare and save by December?"""
    total_savings = 0
    for i in range(12):
        savings = 2**i
        total_savings += savings
    result = total_savings
    return result

print(solution())