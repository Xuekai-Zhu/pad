def solution():
    """Kate loves painting. She decided to go to an Art-museum in her city. The entrance fee is $5. Kate loved the visit so much, that she decided to go there once a month. After 1 year, the ticket price increased to $7 and Kate decided she is going to visit the museum only 4 times a year. How much did Kate pay for all visits to the Art-museum after 3 years of visiting?"""
    # Define the initial ticket price and the number of visits per year
    ticket_price = 5
    visits_per_year = 12

    # Calculate the total cost of visiting the museum for the first year
    total_cost_first_year = ticket_price * visits_per_year

    # Define the new ticket price and the new number of visits per year
    new_ticket_price = 7
    new_visits_per_year = 4

    # Calculate the total cost of visiting the museum for the second and third year combined
    total_cost_second_and_third_year = new_ticket_price * new_visits_per_year * 2

    # Calculate the total cost of visiting the museum for three years
    total_cost = total_cost_first_year + total_cost_second_and_third_year

    result = total_cost
    return result

print(solution())