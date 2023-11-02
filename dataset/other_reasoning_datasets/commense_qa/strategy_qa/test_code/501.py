def solution():
    harry_potter_author = "J.K. Rowling"
    actor_who_played_snape = "Alan Rickman"
    if actor_who_played_snape in harry_potter_author:
        result = "yes"
    else:
        result = "no"
    return result

print(solution())