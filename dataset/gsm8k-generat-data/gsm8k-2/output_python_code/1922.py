def solution():
    """Katrina saw an ad that said if she signed up for her local recycling program, she could earn $5.00. When she signed up, they told her for every friend that she referred, the friend would receive $5.00 and she would receive another $5.00 per friend. That day, she had 5 friends sign up and another 7 friends by the end of the week. How much money in total did she and her friends make?"""
    katrina_earnings = 5
    friend_earnings = 5
    num_signups_day = 5
    num_signups_week = 7
    total_earnings = katrina_earnings + (friend_earnings * (num_signups_day + num_signups_week))
    result = total_earnings
    return result

print(solution())