def solution():
    mother_duck = 8
    first_three_ducklings = 3
    snail_amount_first_three = first_three_ducklings * 5
    second_three_ducklings = 3
    snail_amount_second_three = second_three_ducklings * 9
    remaining_ducklings = mother_duck - first_three_ducklings - second_three_ducklings
    snail_amount_remaining = remaining_ducklings * (5/2)
    total_snail_amount = snail_amount_first_three + snail_amount_second_three + snail_amount_remaining
    result = total_snail_amount
    return result

print(solution())