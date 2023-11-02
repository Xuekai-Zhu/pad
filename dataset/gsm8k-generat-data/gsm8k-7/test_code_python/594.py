def solution():
    initial_shells = 2

    ed_limpet_shells = 7
    ed_oyster_shells = 2
    ed_conch_shells = 4

    jacob_total_shells = (ed_limpet_shells + ed_oyster_shells + ed_conch_shells) + 2

    total_shells = initial_shells + ed_limpet_shells + ed_oyster_shells + ed_conch_shells + jacob_total_shells

    result = total_shells
    return result

print(solution())