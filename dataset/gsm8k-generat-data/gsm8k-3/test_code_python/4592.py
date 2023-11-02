def solution():
    """
    Jodi and Vance are researching on a deserted island and have to stay
    on the island for a certain number of weeks to carry out their research.
    On their first expedition, they stayed for three weeks on the island. They
    spent two weeks more on the second expedition than they spent on their
    first expedition. They spent twice as many weeks on their last expedition
    as they spent on their second expedition. Calculate the total number of
    days they spent on the island on all the trips.
    """
    # Calculate the number of weeks on the second expedition
    second_exp_weeks = 3 + 2

    # Calculate the number of weeks on the last expedition
    last_exp_weeks = 2 * second_exp_weeks

    # Calculate the total number of weeks on all expeditions
    total_weeks = 3 + second_exp_weeks + last_exp_weeks

    # Calculate the total number of days on the island
    total_days = total_weeks * 7

    # Display the total number of days
    result = total_days
    return result

print(solution())