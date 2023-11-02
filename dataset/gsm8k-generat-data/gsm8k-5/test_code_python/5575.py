def solution():
    jade_money = 38  # Jade had $38
    julia_money = jade_money / 2  # Julia had half as much money as Jade
    total_money = 97  # Their aunt gave them a total of $97
    initial_total = jade_money + julia_money  # Total money they had before their aunt gave them money

    # Calculate the total amount of money their aunt gave them
    aunt_money = total_money - initial_total

    # Divide the aunt's money equally between Jade and Julia
    aunt_per_person = aunt_money / 2
    result = aunt_per_person
    return result

print(solution())