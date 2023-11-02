def solution():
    # Define the flight time from NYC to Chicago and the layover in Chicago
    nyc_to_chicago = 4
    chicago_layover = 1

    # Calculate the flight time from Chicago to Miami
    chicago_to_miami = 3 * nyc_to_chicago

    # Calculate the total travel time
    total_time = nyc_to_chicago + chicago_layover + chicago_to_miami

    result = total_time
    return result

print(solution())