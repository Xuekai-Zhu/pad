def solution():
    # Calculate how much money Juanita makes from hitting 200 drums
    money_from_200_drums = 200 * 0.025

    # Calculate how much money Juanita lost by joining the contest
    lost_money = 10 + 7.5

    # Calculate how many drums Juanita needs to hit to break even
    break_even_drums = lost_money / 0.025

    # Calculate how many drums Juanita hits to make money
    money_drums = 200 - break_even_drums

    result = money_drums
    return result

print(solution())