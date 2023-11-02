def solution():
    athena_greek = "war"
    aphrodite_greek = "love"
    freya_norse = ["war", "love", "fertility"]
    if set([athena_greek, aphrodite_greek]) == set(freya_norse):
        result = "yes"
    else:
        result = "no"
    return result

print(solution())