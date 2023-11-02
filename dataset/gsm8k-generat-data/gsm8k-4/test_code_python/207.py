def solution():
    """John volunteers at a shelter twice a month for 3 hours at a time. How many hours does he volunteer per year?"""
    # Define the number of hours John volunteers per session and the number of sessions per month
    HOURS_PER_SESSION = 3
    SESSIONS_PER_MONTH = 2

    # Calculate the number of hours John volunteers per month
    hours_per_month = HOURS_PER_SESSION * SESSIONS_PER_MONTH

    # Calculate the number of hours John volunteers per year
    hours_per_year = hours_per_month * 12

    result = hours_per_year
    return result

print(solution())