def solution():
    # Let H be Hannah's current age and J be July's current age
    # We know that H - 20 = 2(J - 20), and H = 2J when H was 6 years old

    # Solving for J, we get J = 23
    J = (20 + 6) / 2

    # July's husband is 2 years older than her, so his age is 25
    husband_age = J + 2
    
    result = husband_age
    return result

print(solution())