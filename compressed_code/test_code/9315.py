def solution():
    
    total_debt = 40
    lulu_savings = 6
    nora_savings = lulu_savings * 5
    tamara_savings = nora_savings / 3
    total_savings = lulu_savings + nora_savings + tamara_savings
    remaining_money = total_savings - total_debt
    each_girl_gets = remaining_money / 3
    result = each_girl_gets

    return result

print(solution())