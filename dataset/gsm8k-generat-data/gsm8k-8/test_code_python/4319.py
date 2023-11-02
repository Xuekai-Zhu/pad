def solution():
    # Calculate the total number of oranges Tammy can pick in one day
    oranges_per_day = 10 * 12
   
    # Calculate the total number of oranges Tammy can pick in three weeks
    oranges_in_3_weeks = oranges_per_day * 21
    
    # Calculate the total number of 6-packs of oranges Tammy can sell
    six_packs = oranges_in_3_weeks // 6
    
    # Calculate the total amount of money Tammy will earn
    money_earned = six_packs * 2
    
    result = money_earned
    return result

print(solution())