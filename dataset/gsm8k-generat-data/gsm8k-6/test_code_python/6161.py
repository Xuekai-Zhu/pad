def solution():
    # Calculate Jermaine's earnings
    jermaine_earnings = 30 + 5  # Jermaine earns $5 more than Terrence
    
    # Calculate the total earnings of Jermaine, Terrence, and Emilee
    total_earnings = jermaine_earnings + 30 + emilee_earnings
    
    # Calculate Emilee's earnings
    emilee_earnings = 90 - total_earnings
    
    result = emilee_earnings
    return result

print(solution())