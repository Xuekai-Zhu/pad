def solution():
    # Calculate the total amount of money Kendall has in cents
    total_cents = 10*25 + 12*10  # Kendall has 10 quarters and 12 dimes
    # Calculate the amount of money Kendall has in nickels in cents
    nickels_cents = (400 - total_cents) // 5
    result = nickels_cents // 5
    return result

print(solution())