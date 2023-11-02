def solution():
    lulu_savings = 6  # Lulu has saved $6
    nora_savings = 5 * lulu_savings  # Nora has saved five times what Lulu has
    tamara_savings = nora_savings / 3  # Tamara's savings are three times less than Nora's
    total_savings = lulu_savings + nora_savings + tamara_savings  # Total savings of all three girls
    remaining_money = total_savings - 40  # They pay off a $40 debt
    girls_share = remaining_money / 3  # Divide the remaining money equally among the girls
    result = girls_share
    return result

print(solution())