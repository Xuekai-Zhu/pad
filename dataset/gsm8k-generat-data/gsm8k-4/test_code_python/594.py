def solution():
    """Ed and Jacob already had 2 shells in their shell collection. Then they went to the beach to collect even more. Ed found 7 limpet shells, 2 oyster shells, and 4 conch shells. Jacob found 2 more shells than Ed did. How many shells do the pair have altogether?"""
    # Define the initial number of shells
    initial_shells = 2

    # Define the number of shells found by Ed
    ed_limpets = 7
    ed_oysters = 2
    ed_conchs = 4

    # Calculate the number of shells found by Jacob
    jacob_total = (ed_limpets + ed_oysters + ed_conchs) + 2

    # Calculate the total number of shells
    total_shells = initial_shells + ed_limpets + ed_oysters + ed_conchs + jacob_total

    result = total_shells
    return result

print(solution())