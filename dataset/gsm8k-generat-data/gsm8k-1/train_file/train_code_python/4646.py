def solution():
    """Monica was saving money for her future. Every week he put $15 into her moneybox. 
    After the moneybox got full, which took 60 weeks, Monica took all the money out and took it to the bank, 
    and she started saving money again. She repeated this whole process 5 times. How much money did Monica 
    take to the bank in total?"""
    money_saved_per_week = 15
    weeks_to_fill_box = 60
    total_savings_per_box = money_saved_per_week * weeks_to_fill_box
    num_boxes = 5
    total_savings = total_savings_per_box * num_boxes
    result = total_savings
    return result

print(solution())