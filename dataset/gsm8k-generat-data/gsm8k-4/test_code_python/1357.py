def solution():
    """Lizzy's mother gave her 80 cents and her father gave her 40 cents for keeping to her promise. She went to her uncle's and spent 50 cents buying candy for her little cousin. Her uncle gave her another 70 cents. How many cents does she have now?"""
    # Define the initial amount of money Lizzy had
    initial_money = 80 + 40

    # Subtract the amount of money spent on candy
    money_after_candy = initial_money - 50

    # Add the money given by her uncle
    final_money = money_after_candy + 70

    # return the result in cents
    result = final_money * 100
    return result

print(solution())