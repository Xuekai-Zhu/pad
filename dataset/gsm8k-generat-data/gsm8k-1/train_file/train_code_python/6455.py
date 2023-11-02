def solution():
    """Mr. and Mrs. McPherson have to renew their rent by the end of the year. They agreed that Mrs. McPherson would raise 30% of the money. If their rent is $1200 per year, how much does Mr. McPherson need to raise to complete the rent?"""
    total_rent = 1200
    mrs_mcpherson_percent = 30
    mrs_mcpherson_amount = total_rent * (mrs_mcpherson_percent / 100)
    mr_mcpherson_amount = total_rent - mrs_mcpherson_amount
    result = mr_mcpherson_amount
    return result

print(solution())