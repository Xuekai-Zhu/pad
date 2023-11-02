def solution():
    fair_trade_involves_fair_prices_to_producers = True
    english_lords_and_peasants_relationship_was_indentured_servitude = True
    if fair_trade_involves_fair_prices_to_producers and not english_lords_and_peasants_relationship_was_indentured_servitude:
        result = "yes"
    else:
        result = "no"
    return result

print(solution())