def solution():
    jade_money = 38
    julia_money = jade_money / 2
    total_money = 97

    # Calculate total money before their aunt gave them money
    initial_total_money = jade_money + julia_money

    # Calculate amount given by their aunt to each of them
    aunt_money = (total_money - initial_total_money) / 2
    result = aunt_money
    return result

print(solution())