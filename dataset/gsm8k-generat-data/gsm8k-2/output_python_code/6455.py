def solution():
    """Mr. and Mrs. McPherson have to renew their rent by the end of the year. They agreed that Mrs. McPherson would raise 30% of the money. If their rent is $1200 per year, how much does Mr. McPherson need to raise to complete the rent?"""
    rent = 1200
    mrs_mcpherson_contribution = 0.3 * rent
    mr_mcpherson_contribution = rent - mrs_mcpherson_contribution
    result = mr_mcpherson_contribution
    return result

print(solution())