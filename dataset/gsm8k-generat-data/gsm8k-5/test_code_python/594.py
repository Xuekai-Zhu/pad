def solution():
    initial_shells = 2  # Ed and Jacob already have 2 shells
    ed_limpet_shells = 7
    ed_oyster_shells = 2
    ed_conch_shells = 4
    ed_total_shells = ed_limpet_shells + ed_oyster_shells + ed_conch_shells  # Ed's total number of shells
    jacob_total_shells = ed_total_shells + 2  # Jacob found 2 more shells than Ed
    total_shells = initial_shells + ed_total_shells + jacob_total_shells  # Calculate the total number of shells
    result = total_shells
    return result

print(solution())