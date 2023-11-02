def solution():
    
    # Define the number of checks written per month for each service
    electric_checks = 12
    gas_checks = 12
    church_checks = 2 * electric_checks
    pest_lawn_checks = 0.25 * gas_checks

    # Calculate the total number of checks written per year
    total_checks = electric_checks + gas_checks + church_checks + pest_lawn_checks

    # Display the total number of checks written per year
    result = total_checks
    return result

print(solution())