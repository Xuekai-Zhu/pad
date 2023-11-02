def solution():
    first_expedition = 3  # Jodi and Vance stayed for 3 weeks on their first expedition
    second_expedition = first_expedition + 2  # They stayed 2 weeks more on their second expedition
    third_expedition = 2 * (second_expedition + 2)  # They stayed twice as many weeks on their last expedition as they did on their second expedition
    total_weeks = first_expedition + second_expedition + third_expedition  # Calculate the total number of weeks they spent on the island
    total_days = total_weeks * 7  # Convert the total number of weeks to days
    result = total_days
    return result

print(solution())