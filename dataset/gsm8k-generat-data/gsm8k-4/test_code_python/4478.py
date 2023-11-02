def solution():
    """Tamara, Nora, and Lulu have been saving to pay off a $40 debt. So far, Nora has saved five times what Lulu has, but three times Tamara’s savings.  Lulu has saved $6. If they pay off the debt and divide the remaining money equally, how many dollars will each girl get?"""
    # Define Lulu's savings
    lulu_savings = 6

    # Calculate Nora's savings
    nora_savings = 5 * lulu_savings

    # Calculate Tamara's savings
    tamara_savings = nora_savings / 3

    # Calculate the total savings
    total_savings = lulu_savings + nora_savings + tamara_savings

    # Calculate the money each girl will get after paying off the debt
    remaining_money = total_savings - 40
    each_girl_money = remaining_money / 3

    # Return the result
    result = each_girl_money
    return result

print(solution())