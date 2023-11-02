def solution():
    growth_rate = 3  # Haley grows at the rate of 3 inches every year
    current_height = 20  # Haley is currently 20 inches tall
    years = 10  # Haley wants to know her height after 10 years

    # Calculate Haley's height after 10 years
    future_height = current_height + (growth_rate * years)

    result = future_height
    return result

print(solution())