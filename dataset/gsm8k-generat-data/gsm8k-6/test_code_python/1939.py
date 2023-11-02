def solution():
    # Calculate Jerome's initial amount of money
    initial_money = 2 * 43  # half of Jerome's money was $43

    # Calculate how much Jerome gave to Meg
    jerome_after_meg = initial_money - 8

    # Calculate how much Jerome gave to Bianca
    jerome_after_bianca = jerome_after_meg - (3 * 8)  # thrice as much as what he gave to Meg

    # Calculate how much money Jerome has left
    jerome_remaining = jerome_after_bianca

    result = jerome_remaining
    return result

print(solution())