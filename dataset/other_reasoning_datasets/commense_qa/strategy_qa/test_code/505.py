def solution():
    # Define Christopher Nolan's involvement with Batman and Bob Kane's co-creation of the character
    nolan_batman_movies = True
    bob_kane_creator = True
    # Check if Nolan is indebted to Kane
    if nolan_batman_movies and bob_kane_creator:
        result = "yes"
    else:
        result = "no"
    return result

print(solution())