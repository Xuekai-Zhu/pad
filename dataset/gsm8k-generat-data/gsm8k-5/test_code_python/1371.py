def solution():
    total_money = 10000  # Natalie's father has saved up $10,000
    natalie_share = total_money / 2  # Natalie gets half of the total money
    remaining_money = total_money - natalie_share  # Calculate the remaining money after Natalie gets her share
    rick_share = 0.6 * remaining_money  # Rick gets 60% of the remaining money
    lucy_share = total_money - natalie_share - rick_share  # Lucy gets whatever is left after Natalie and Rick get paid

    result = lucy_share
    return result

print(solution())