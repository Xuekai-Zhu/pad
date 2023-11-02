def solution():
    """Jake trips over his dog 40% percent of mornings. 25% of the time he trips, he drops his coffee. What percentage of mornings does he NOT drop his coffee?"""
    # Define the probability of tripping over the dog and dropping coffee
    p_trip = 0.4
    p_drop_given_trip = 0.25

    # Calculate the probability of not dropping coffee
    p_not_drop_given_trip = 1 - p_drop_given_trip
    p_not_drop = (1 - p_trip) + (p_trip * p_not_drop_given_trip)

    # Convert to percentage and round to 2 decimal places
    result = round(p_not_drop * 100, 2)
    return result

print(solution())