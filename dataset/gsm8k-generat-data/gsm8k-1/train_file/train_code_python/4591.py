def solution():
    """Jodi and Vance are researching on a deserted island and have to stay on the island for a certain number of weeks to carry out their research. On their first expedition, they stayed for three weeks on the island. They spent two weeks more on the second expedition than they spent on their first expedition. They spent twice as many weeks on their last expedition as they spent on their second expedition. Calculate the total number of days they spent on the island on all the trips."""
    first_exp = 3
    second_exp = first_exp + 2
    last_exp = second_exp * 2
    total_weeks = first_exp + second_exp + last_exp
    total_days = total_weeks * 7
    result = total_days
    return result

print(solution())