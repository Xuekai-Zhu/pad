def solution():
    """Steve wanted to make a total of $100 within four days, so he took on a berry-picking job in Sweden. The job paid $2 for every pound of lingonberries picked. On Monday he picked 8 pounds. Tuesday’s harvest was triple what he had picked the previous day. On Wednesday he felt very tired and decided to rest. How many pounds of lingonberries did Steve have to pick on Thursday?"""
    total_days = 4
    target_money = 100
    money_per_pound = 2
    
    # Calculate how much money Steve already made
    monday_pounds = 8
    monday_money = monday_pounds * money_per_pound
    
    tuesday_pounds = monday_pounds * 3
    tuesday_money = tuesday_pounds * money_per_pound
    
    wednesday_money = 0  # Steve rested
    
    total_money = monday_money + tuesday_money + wednesday_money
    
    # Calculate how much money Steve still needs to make
    remaining_money = target_money - total_money
    
    # Calculate how many pounds Steve needs to pick on Thursday
    pounds_needed = remaining_money / money_per_pound
    result = pounds_needed
    
    return result

print(solution())