def solution():
    """The school decided to have a fundraiser to collect $750 for new basketball equipment. Families could donate $25, $50, or $100. Families who donated $25 got Bronze Status. Families who donated $50 got Silver Status. Families who donated $100 got Gold Status. With one day left in the fundraiser, the school has 10 Bronze Status families, 7 Silver Status Families and 1 Gold Status family. How much do they need to raise on the final day to reach their goal?"""
    goal_amount = 750
    bronze_count = 10
    silver_count = 7
    gold_count = 1
    bronze_amount = 25
    silver_amount = 50
    gold_amount = 100
    current_amount = bronze_amount * bronze_count + silver_amount * silver_count + gold_amount * gold_count
    remaining_amount = goal_amount - current_amount
    result = remaining_amount
    
    return result

print(solution())