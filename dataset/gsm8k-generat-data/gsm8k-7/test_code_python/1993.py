def solution():
    georgia_coughs_per_minute = 5
    robert_coughs_per_minute = 2 * georgia_coughs_per_minute
    num_minutes = 20

    # Calculate the total number of times Georgia coughs in 20 minutes
    georgia_total_coughs = georgia_coughs_per_minute * num_minutes

    # Calculate the total number of times Robert coughs in 20 minutes
    robert_total_coughs = robert_coughs_per_minute * num_minutes

    # Calculate the total number of times they both cough in 20 minutes
    total_coughs = georgia_total_coughs + robert_total_coughs
    result = total_coughs
    return result

print(solution())