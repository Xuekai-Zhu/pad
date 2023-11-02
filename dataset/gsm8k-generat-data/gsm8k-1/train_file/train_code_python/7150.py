def solution():
    """Kate loves painting. She decided to go to an Art-museum in her city. The entrance fee is $5. Kate loved the visit so much, that she decided to go there once a month. After 1 year, the ticket price increased to $7 and Kate decided she is going to visit the museum only 4 times a year. How much did Kate pay for all visits to the Art-museum after 3 years of visiting?"""
    price_per_visit_year1 = 5
    price_per_visit_year2 = 7
    visits_per_month = 1
    months_per_year = 12
    visits_per_year_year1 = visits_per_month * months_per_year
    visits_per_year_year2 = 4
    total_visits = visits_per_year_year1 + visits_per_year_year2 * 2
    total_cost = visits_per_year_year1 * price_per_visit_year1 + visits_per_year_year2 * price_per_visit_year2
    result = total_cost * 3
    return result

print(solution())