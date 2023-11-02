def solution():
    # Calculate Michiko's score
    michiko_score = 14 / 2

    # Calculate Akiko's score
    akiko_score = michiko_score + 4

    # Calculate Chandra's score
    chandra_score = 2 * akiko_score

    # Calculate the total team score
    total_score = michiko_score + akiko_score + chandra_score + 14

    result = total_score
    return result

print(solution())