def solution():
    """Jeans makeup artist charges her $250 an hour. She requires very expensive makeup for a movie she is in and it takes 6 hours to do each day and she needs it done 4 times a week. The movie takes 5 weeks to finish. After the movie is done the makeup artist gives Jean a 10% discount because of the amount of work done. How much did Jean pay?"""
    hourly_rate = 250
    hours_per_day = 6
    days_per_week = 4
    weeks = 5
    total_hours = hours_per_day * days_per_week * weeks
    total_cost = hourly_rate * total_hours
    discount = 0.1
    discounted_cost = total_cost - (total_cost * discount)
    result = discounted_cost
    return result

print(solution())