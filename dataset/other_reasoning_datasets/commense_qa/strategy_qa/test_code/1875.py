def solution():
    abba_genre = "Disco"
    current_genre = ["Disco", "Funk"]
    if abba_genre in current_genre:
        result = "yes"
    else:
        result = "no"
    return result

print(solution())