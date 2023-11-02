def solution():
    bailey_score = 14

    # Calculate Michiko's score
    michiko_score = bailey_score / 2

    # Calculate Akiko's score
    akiko_score = michiko_score + 4

    # Calculate Chandra's score
    chandra_score = akiko_score * 2

    # Calculate the total team score
    total_score = bailey_score + michiko_score + akiko_score + chandra_score
    result = total_score
    return result

print(solution())