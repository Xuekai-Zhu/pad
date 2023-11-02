def solution():
    # Calculate Nora and Tamara's savings
    lulu_savings = 6
    nora_savings = 5 * lulu_savings
    tamara_savings = nora_savings / 3

    # Calculate the total savings and remaining amount after paying off debt
    total_savings = lulu_savings + nora_savings + tamara_savings
    remaining_amount = total_savings - 40

    # Calculate the amount each girl will get after dividing the remaining amount equally
    each_girl_gets = remaining_amount / 3
    result = each_girl_gets
    return result

print(solution())