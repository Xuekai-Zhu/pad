def solution():
    paramount_leader = "highest leader of China"
    titanic_producer = "Paramount Pictures"
    paramount_leader_nationality = "Chinese"
    titanic_producer_nationality = "American"
    if titanic_producer_nationality == "American" and paramount_leader_nationality == "Chinese":
        result = "no"
    else:
        result = "unknown"
    return result

print(solution())