def solution():
    # Calculate the total number of shells collected by Ed
    ed_shells = 7 + 2 + 4  # Ed found 7 limpet shells, 2 oyster shells, and 4 conch shells

    # Calculate the total number of shells collected by Jacob
    jacob_shells = ed_shells + 2  # Jacob found 2 more shells than Ed did

    # Calculate the total number of shells collected by both
    total_shells = 2 + ed_shells + jacob_shells  # Ed and Jacob already had 2 shells in their collection

    result = total_shells
    return result

print(solution())