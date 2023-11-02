def solution():
    """Anna has 3 times as many toys as Mandy and 2 fewer toys than Amanda. If they have 142 toys all together, how many toys does Mandy have?"""
    total_toys = 142
    anna_toys = 3 * mandy_toys
    amanda_toys = anna_toys + 2
    mandy_toys = (total_toys - amanda_toys - anna_toys) / 3
    result = mandy_toys
    return result

print(solution())