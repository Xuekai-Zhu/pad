def solution():
    
    witch_votes = 7
    unicorn_votes = 3 * witch_votes
    dragon_votes = witch_votes + 25
    total_votes = witch_votes + unicorn_votes + dragon_votes
    result = total_votes
    return result

print(solution())