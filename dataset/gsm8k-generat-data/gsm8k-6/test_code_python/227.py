def solution():
    ian_money = 100  # Initial amount won in the lottery
    colin_payment = 20  # Payment made to Colin
    helen_payment = 2 * colin_payment  # Payment made to Helen, twice as much as Colin
    benedict_payment = helen_payment / 2  # Payment made to Benedict, half as much as Helen
    total_payment = colin_payment + helen_payment + benedict_payment  # Total payment made
    remaining_money = ian_money - total_payment  # Money remaining after paying off debts
    result = remaining_money
    return result

print(solution())