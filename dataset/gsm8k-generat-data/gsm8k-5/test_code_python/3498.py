def solution():
    # Calculate the total contribution from Harry and his friends
    total_contribution = 3 * (30 + (3 * 7))  # Harry added $30 and 3 weeks is equivalent to $21 (3 * 7)
    
    # Calculate the individual contribution from each of Harry's friends
    friends_contribution = total_contribution / 3
    result = friends_contribution
    return result

print(solution())