def solution():
    """Tamara, Nora, and Lulu have been saving to pay off a $40 debt. So far, Nora has saved five times what Lulu has, but three times Tamara’s savings. Lulu has saved $6. If they pay off the debt and divide the remaining money equally, how many dollars will each girl get?"""
    # Define Lulu's savings and calculate Nora's and Tamara's savings
    LULU_SAVINGS = 6
    NORA_SAVINGS = LULU_SAVINGS * 5
    TAMARA_SAVINGS = NORA_SAVINGS / 3

    # Calculate the total savings
    total_savings = LULU_SAVINGS + NORA_SAVINGS + TAMARA_SAVINGS

    # Calculate the amount each girl will get after paying off the debt
    remaining_money = total_savings - 40
    each_girl_gets = remaining_money / 3

    # Display the amount each girl will get
    result = each_girl_gets
    return result

print(solution())