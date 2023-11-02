def solution():
    """Ed and Jacob already had 2 shells in their shell collection. Then they went to the beach to collect even more. Ed found 7 limpet shells, 2 oyster shells, and 4 conch shells. Jacob found 2 more shells than Ed did. How many shells do the pair have altogether?"""
    # Define the number of shells Ed found
    ed_limpets = 7
    ed_oysters = 2
    ed_conchs = 4

    # Calculate the total number of shells Ed found
    ed_total = ed_limpets + ed_oysters + ed_conchs

    # Calculate the number of shells Jacob found
    jacob_total = ed_total + 2

    # Calculate the total number of shells the pair has
    total_shells = 2 + ed_total + jacob_total

    # Display the total number of shells
    result = total_shells
    return result

print(solution())