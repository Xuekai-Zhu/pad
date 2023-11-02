def solution():
    """Kate loves painting. She decided to go to an Art-museum in her city. The entrance fee is $5. Kate loved the visit so much, that she decided to go there once a month. After 1 year, the ticket price increased to $7 and Kate decided she is going to visit the museum only 4 times a year. How much did Kate pay for all visits to the Art-museum after 3 years of visiting?"""
    # Define the initial entrance fee and the number of visits per year
    entrance_fee = 5
    visits_per_year = 12

    # Calculate Kate's total cost for the first year
    total_cost = entrance_fee * visits_per_year

    # Update the entrance fee and visits per year for the following years
    entrance_fee = 7
    visits_per_year = 4

    # Calculate Kate's total cost for each following year and add it to the previous total cost
    for i in range(2, 5):
        year_cost = entrance_fee * visits_per_year
        total_cost += year_cost

    # Display Kate's total cost for all visits to the Art-museum after 3 years of visiting
    result = total_cost
    return result

print(solution())