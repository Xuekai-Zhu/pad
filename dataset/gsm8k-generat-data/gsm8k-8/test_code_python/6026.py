def solution():
    # Calculate the total number of burritos
    total_burritos = 3 * 20

    # Calculate the number of burritos given away
    given_burritos = total_burritos / 3

    # Calculate the number of burritos eaten by John
    eaten_burritos = 3 * 10

    # Calculate the number of burritos left
    remaining_burritos = total_burritos - given_burritos - eaten_burritos
    result = remaining_burritos
    return result

print(solution())