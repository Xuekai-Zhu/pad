def solution():
    
    oranges = 80
    pieces_per_orange = 10
    pieces_per_friend = 4
    friends = (oranges * pieces_per_orange) // pieces_per_friend
    result = friends
    return result

print(solution())