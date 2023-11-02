def solution():
    cost_to_enter = 10  # Juanita paid $10 to enter the contest
    money_lost = 7.5  # Juanita lost $7.50 from joining the contest
    drums_for_money = 200  # Juanita needs to hit 200 drums to start earning money
    money_per_drum = 0.025  # Juanita earns 2.5 cents per drum hit

    # Calculate the total money Juanita earns
    total_money = (drums_for_money * money_per_drum) - cost_to_enter - money_lost

    # Calculate the number of drums Juanita hit
    drums_hit = (total_money / money_per_drum) + drums_for_money

    result = drums_hit
    return result

print(solution())