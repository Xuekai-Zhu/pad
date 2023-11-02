def solution():
    total_burritos = 600
    num_students = 50
    burritos_per_student = 10
    num_eating = 20

    # Calculate the total number of burritos given away
    total_given_away = num_students * burritos_per_student

    # Calculate the number of leftover burritos
    leftover_burritos = total_burritos - total_given_away
    result = leftover_burritos
    return result

print(solution())