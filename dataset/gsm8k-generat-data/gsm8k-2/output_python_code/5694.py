def solution():
    """One hundred chips were divided by Ian and Lyle in the ratio 4:6. What percentage of the chips did Lyle have?"""
    total_chips = 100
    lyle_ratio = 6 / 10 # Lyle's share of the chips out of the total ratio
    lyle_chips = total_chips * lyle_ratio
    percentage_lyle = lyle_chips / total_chips * 100
    result = percentage_lyle
    return result

print(solution())