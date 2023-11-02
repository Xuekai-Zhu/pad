def solution():
    # Define the toilet paper production before the increase
    original_production = 7000

    # Define the increase in production
    production_increase = 3

    # Calculate the total production after the increase
    total_production = original_production * production_increase

    # Calculate the total production for March of 2020 (31 days)
    march_production = total_production * 31

    result = march_production
    return result

print(solution())