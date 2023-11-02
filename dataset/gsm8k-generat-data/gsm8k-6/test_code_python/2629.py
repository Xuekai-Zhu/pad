def solution():
    # Set up the equation for the given information
    # Hajar's score + (Hajar's score + 21) = 24*2
    # Simplify and solve for Hajar's score
    hajar_score = (24*2 - 21)/2
    farah_score = hajar_score + 21
    total_score = hajar_score + farah_score
    result = total_score
    return result

print(solution())