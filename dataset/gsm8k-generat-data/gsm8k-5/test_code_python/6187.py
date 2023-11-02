def solution():
    closing_dow = 8722  # Dow closed at 8,722
    percent_change = 0.02  # Dow fell 2%
    opening_dow = closing_dow / (1 - percent_change)  # Calculate opening Dow using the percent change formula
    result = opening_dow
    return result

print(solution())