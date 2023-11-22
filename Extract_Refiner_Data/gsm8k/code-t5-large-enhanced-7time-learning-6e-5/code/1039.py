def solution():
    
    # Define the number of countries and cities
    num_countries = 26
    num_cities_per_country = 5

    # Define the number of people living in each city
    people_per_city = 1000

    # Calculate the total number of people living in the cities
    total_people = num_cities_per_country * people_per_city * num_countries

    # return the result
    result = total_people
    return result

print(solution())