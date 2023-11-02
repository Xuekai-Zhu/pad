def solution():
    """Sarah starts saving $5.00 a week for 4 weeks. Then she saves $10.00 a week for the next 4 weeks. Then she saves $20.00 a week for the next 4 weeks. How much money has she saved over 12 weeks?"""
    weeks = [4, 4, 4]
    amounts = [5, 10, 20]
    total_savings = 0
    for i in range(len(weeks)):
        total_savings += weeks[i] * amounts[i]
    result = total_savings
    return result

print(solution())