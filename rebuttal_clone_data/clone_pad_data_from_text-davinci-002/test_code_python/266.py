def solution():
    """Johns goes to the gym 3 times a week. He spends 1 hour each day lifting weight. Additionally, he also spends a third of his weightlifting time warming up and doing cardio each day. How many hours does he spend at the gym a week?"""
    days_per_week = 3
    lifting_hours = 1
    cardio_hours = lifting_hours / 3
    total_hours = lifting_hours + cardio_hours
    result = total_hours * days_per_week
    return result

print(solution())