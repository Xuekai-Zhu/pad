def solution():
    # Calculate the number of days Jaylen can feed her dog with the 32 cups bag of dog food
    cups_per_day = 1 + 1  # Jaylen's dog eats 1 cup in the morning and 1 cup in the evening
    days = 32 / cups_per_day
    result = days
    return result

print(solution())