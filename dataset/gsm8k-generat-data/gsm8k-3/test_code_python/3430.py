def solution():
    """Samantha sleeps an average of 8 hours a night. Her baby sister sleeps 2.5 times as much as Samantha does. Because her father is so tired from watching the baby, for every hour the baby sleeps, he sleeps 30 minutes. How many hours does her father sleep in a week?"""
    # Calculate the total number of hours Samantha's sister sleeps per night
    sister_hours = 2.5 * 8

    # Calculate the total number of hours the baby sleeps per week
    baby_hours = sister_hours * 7

    # Calculate the total number of hours Samantha's father sleeps per hour the baby sleeps
    father_hours = baby_hours * 0.5

    # Display the total number of hours Samantha's father sleeps in a week
    result = father_hours
    return result

print(solution())