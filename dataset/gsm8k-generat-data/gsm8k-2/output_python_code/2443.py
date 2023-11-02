def solution():
    """The school decided to have a fundraiser to collect $750 for new basketball equipment. Families could donate $25, $50, or $100. Families who donated $25 got Bronze Status. Families who donated $50 got Silver Status. Families who donated $100 got Gold Status. With one day left in the fundraiser, the school has 10 Bronze Status families, 7 Silver Status Families and 1 Gold Status family. How much do they need to raise on the final day to reach their goal?"""
    bronze_donation = 25
    silver_donation = 50
    gold_donation = 100
    bronze_count = 10
    silver_count = 7
    gold_count = 1
    total_raised = (bronze_count * bronze_donation) + (silver_count * silver_donation) + (gold_count * gold_donation)
    remaining_goal = 750 - total_raised
    result = remaining_goal
    return result

print(solution())