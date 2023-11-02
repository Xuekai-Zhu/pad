def solution():
    """Kate loves painting. She decided to go to an Art-museum in her city. The entrance fee is $5. Kate loved the visit so much, that she decided to go there once a month. After 1 year, the ticket price increased to $7 and Kate decided she is going to visit the museum only 4 times a year. How much did Kate pay for all visits to the Art-museum after 3 years of visiting?"""
    first_year_visits = 12
    second_year_visits = 12
    third_year_visits = 36 - first_year_visits - second_year_visits
    first_year_price = first_year_visits * 5
    second_year_price = second_year_visits * 5 + (12 - second_year_visits) * 7
    third_year_price = third_year_visits * 4 * 7

    total_price = first_year_price + second_year_price + third_year_price

    result = total_price
    return result

print(solution())