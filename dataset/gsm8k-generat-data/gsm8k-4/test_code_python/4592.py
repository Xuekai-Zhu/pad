def solution():
    """Jodi and Vance are researching on a deserted island and have to stay on the island for a certain number of weeks to carry out their research. On their first expedition, they stayed for three weeks on the island. They spent two weeks more on the second expedition than they spent on their first expedition. They spent twice as many weeks on their last expedition as they spent on their second expedition. Calculate the total number of days they spent on the island on all the trips."""
    # Define the number of weeks spent on each expedition
    first_weeks = 3
    second_weeks = first_weeks + 2
    last_weeks = second_weeks * 2

    # Calculate the total number of weeks spent on the island
    total_weeks = first_weeks + second_weeks + last_weeks

    # Calculate the total number of days spent on the island
    total_days = total_weeks * 7

    # return the result
    result = total_days
    return result

print(solution())