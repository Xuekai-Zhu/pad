def solution():
    nora_savings = 5 * lulu_savings
    tamara_savings = nora_savings / 3
    total_savings = nora_savings + tamara_savings + lulu_savings
    debt = 40
    money_left = total_savings - debt
    dollars_per_girl = money_left / 3
    result = dollars_per_girl
    return result

print(solution())