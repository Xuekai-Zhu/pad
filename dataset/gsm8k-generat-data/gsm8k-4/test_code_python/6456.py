def solution():
    """Mr. and Mrs. McPherson have to renew their rent by the end of the year. They agreed that Mrs. McPherson would raise 30% of the money. If their rent is $1200 per year, how much does Mr. McPherson need to raise to complete the rent?"""
    # Define the total rent and the percentage that Mrs. McPherson will raise
    total_rent = 1200
    mrs_mcpherson_percentage = 0.3

    # Calculate the amount that Mrs. McPherson will raise
    mrs_mcpherson_amount = total_rent * mrs_mcpherson_percentage

    # Calculate the amount that Mr. McPherson needs to raise
    mr_mcpherson_amount = total_rent - mrs_mcpherson_amount

    # return the result
    result = mr_mcpherson_amount
    return result

print(solution())