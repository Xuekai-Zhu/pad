def solution():
    """Gerald thought it would be funny to trick his coworker, who's allergic to peanuts, into eating a peanut butter cookie. When his coworker goes into anaphylactic shock and is taken to the hospital, Gerald is arrested. The judge sentences Gerald to 3 months for assault and 2 years for poisoning, then extends his sentence by 1/3 since this is Gerald's third offense. How many months does Gerald spend in jail?"""
    # Define the initial jail time for assault and poisoning
    assault_time = 3  # in months
    poisoning_time = 24  # in months

    # Calculate the total jail time
    total_time = assault_time + poisoning_time

    # Extend the time by 1/3 for the third offense
    extended_time = total_time + (total_time * (1/3))

    result = round(extended_time)
    return result

print(solution())