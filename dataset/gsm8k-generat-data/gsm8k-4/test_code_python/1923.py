def solution():
    """Katrina saw an ad that said if she signed up for her local recycling program, she could earn $5.00. When she signed up, they told her for every friend that she referred, the friend would receive $5.00 and she would receive another $5.00 per friend. That day, she had 5 friends sign up and another 7 friends by the end of the week. How much money in total did she and her friends make?"""
    # Define the amount earned for signing up
    base_earnings = 5

    # Define the earnings per referred friend
    referral_earnings = 5

    # Calculate the earnings from the initial 5 friends
    initial_earnings = 5 * referral_earnings

    # Calculate the earnings from the additional 7 friends
    additional_earnings = 7 * referral_earnings

    # Calculate the total earnings
    total_earnings = base_earnings + initial_earnings + additional_earnings

    # return the result
    result = total_earnings
    return result

print(solution())