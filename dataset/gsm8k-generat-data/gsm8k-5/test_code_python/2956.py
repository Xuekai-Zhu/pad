def solution():
    attempted_shots = 20  # Cyrus attempted 20 shots
    successful_shots = 0.8 * attempted_shots  # Cyrus made 80% of the shots attempted
    missed_shots = attempted_shots - successful_shots  # Calculate the number of missed shots

    result = missed_shots
    return result

print(solution())