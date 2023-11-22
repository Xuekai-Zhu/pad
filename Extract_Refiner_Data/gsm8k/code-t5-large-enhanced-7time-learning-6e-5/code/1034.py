def solution():
    
    # Define the number of years it takes Jim to finish and the amount of money he earns per year
    years = 4
    loans_per_year = 50000

    # Calculate the total amount of money Jim earns per year
    total_earnings_per_year = loans_per_year * years

    # Calculate the number of years it takes Jim to earn the money equivalent to the loans
    years_to_finish = total_earnings_per_year / 25

    # Calculate the number of years it takes Jim to earn the money equivalent to the loans
    years_to_finish_with_loans = years_to_finish / 25

    # Calculate the total time it takes Jim to earn the money equivalent to the loans
    total_time = years_to_finish + years_to_finish_with_loans

    # Display the total time it takes Jim to earn the money equivalent to the loans
    result = total_time
    return result

print(solution())