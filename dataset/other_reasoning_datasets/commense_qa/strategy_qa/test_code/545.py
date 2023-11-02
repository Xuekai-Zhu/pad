def solution():
    popular_science = True
    peer_review = True 
    if not popular_science and peer_review:
        result = "yes"
    else:
        result = "no"
    return result

print(solution())