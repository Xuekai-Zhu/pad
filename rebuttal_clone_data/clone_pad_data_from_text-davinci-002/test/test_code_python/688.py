def solution():
    bars_of_gold = 60
    gold_tax = bars_of_gold * 0.1
    post_tax_gold = bars_of_gold - gold_tax
    gold_lost_in_divorce = post_tax_gold * 0.5
    post_divorce_gold = post_tax_gold - gold_lost_in_divorce
    result = post_divorce_gold
    return result

print(solution())