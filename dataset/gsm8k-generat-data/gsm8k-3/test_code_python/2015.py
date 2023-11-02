def solution():
    """Mark got a 5% raise at his job.  Before the raise, he earned 40 dollars per hour.  He works 8 hours per day for 5 days per week.  His old bills used to be 600 dollars a week but he decided to add a hundred dollar a week personal trainer.  How much does he have leftover a week?"""
    # Define Mark's hourly wage, number of workdays per week, and hours worked per day
    HOURLY_WAGE = 40
    WORKDAYS_PER_WEEK = 5
    HOURS_PER_DAY = 8

    # Calculate Mark's new hourly wage and weekly salary after the raise
    NEW_HOURLY_WAGE = HOURLY_WAGE * 1.05
    WEEKLY_SALARY = NEW_HOURLY_WAGE * HOURS_PER_DAY * WORKDAYS_PER_WEEK

    # Calculate Mark's new weekly expenses
    OLD_EXPENSES = 600
    PERSONAL_TRAINER_COST = 100
    NEW_EXPENSES = OLD_EXPENSES + PERSONAL_TRAINER_COST

    # Calculate Mark's leftover money after expenses
    LEFTOVER = WEEKLY_SALARY - NEW_EXPENSES

    # Display Mark's weekly leftover money
    result = LEFTOVER
    return result

print(solution())