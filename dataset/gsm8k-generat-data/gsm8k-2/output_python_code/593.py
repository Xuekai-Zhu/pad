def solution():
    """Ed and Jacob already had 2 shells in their shell collection. Then they went to the beach to collect even more. Ed found 7 limpet shells, 2 oyster shells, and 4 conch shells. Jacob found 2 more shells than Ed did. How many shells do the pair have altogether?"""
    ed_total = 2 + 7 + 2 + 4
    jacob_total = ed_total + 2
    total_shells = ed_total + jacob_total
    result = total_shells
    return result

print(solution())