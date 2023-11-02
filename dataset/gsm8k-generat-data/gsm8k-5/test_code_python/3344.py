def solution():
    pennies = 123  # The jar contains 123 pennies
    nickels = 85  # The jar contains 85 nickels
    dimes = 35  # The jar contains 35 dimes
    total_cents = pennies + (nickels * 5) + (dimes * 10)  # Calculate the total number of cents in the jar
    total_cost = 5 * 3 * 2  # Each family member gets a $3 double scoop, and there are 5 family members
    remaining_cents = total_cents - total_cost - 48  # Subtract the total cost and the 48 cents leftover from the trip to get the remaining cents
    quarters = remaining_cents // 25  # Divide the remaining cents by 25 to get the number of quarters in the jar
    result = quarters
    return result

print(solution())