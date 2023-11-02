def solution():
    jess_doubles = 40
    rob_doubles = jess_doubles / 5  # Jess has 5 times as many doubles as Rob
    total_doubles = rob_doubles + jess_doubles
    total_cards = total_doubles / (1/3)  # One third of Rob's cards are doubles
    rob_cards = total_cards - rob_doubles
    result = rob_cards
    return result

print(solution())