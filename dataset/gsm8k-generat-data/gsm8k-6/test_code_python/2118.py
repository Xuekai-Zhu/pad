def solution():
    # Calculate the number of businesses Brandon has left to apply to
    businesses_left = 72 - (72/2) - (72/3)  # half are fired and one third are quit
    result = businesses_left
    return result

print(solution())