def solution():
    """Lizzy's mother gave her 80 cents and her father gave her 40 cents for keeping to her promise. She went to her uncle's and spent 50 cents buying candy for her little cousin. Her uncle gave her another 70 cents. How many cents does she have now?"""
    initial_money = 80 + 40
    spent_money = 50
    additional_money = 70
    total_money = initial_money - spent_money + additional_money
    result = total_money
    return result

print(solution())