def solution():
    initial_amount = 45
    final_amount = initial_amount + 80
    twice_initial = 2 * initial_amount
    remaining_amount = final_amount - twice_initial - 10
    given_away = initial_amount - remaining_amount
    result = given_away
    return result

print(solution())