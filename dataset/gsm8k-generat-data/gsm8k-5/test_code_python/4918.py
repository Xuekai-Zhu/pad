def solution():
    bailey_score = 14  # Bailey scored 14 points
    michiko_score = bailey_score / 2  # Michiko scored half as many points as Bailey
    akiko_score = michiko_score + 4  # Akiko scored 4 more points than Michiko
    chandra_score = akiko_score * 2  # Chandra scored twice as many points as Akiko

    # Calculate the total score for the team
    total_score = bailey_score + michiko_score + akiko_score + chandra_score
    result = total_score
    return result

print(solution())