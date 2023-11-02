def solution():
    # Define the initial number of chickens and the annual increase
    initial_chickens = 550
    annual_increase = 150

    # Calculate the number of chickens after 9 years
    chickens_after_9_years = initial_chickens + (annual_increase * 9)
    result = chickens_after_9_years
    return result

print(solution())