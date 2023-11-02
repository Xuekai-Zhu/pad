def solution():
    """James decides he needs to start eating more vegetables.  He starts by eating a quarter pound of asparagus and a quarter pound of broccoli per day.  After 2 weeks, he doubles that amount and adds 3 pounds of kale per week.  How many pounds of vegetables does he eat a week after adding the kale?"""
    # Define the initial amount of asparagus and broccoli consumed per day
    veggie_per_day = 0.25 + 0.25

    # Define the number of days in two weeks
    days = 14

    # Double the amount of vegetables consumed per day after two weeks
    veggie_per_day *= 2

    # Calculate the total amount of vegetables consumed per week after two weeks
    veggie_per_week = (veggie_per_day * 7) + 3

    # Display the total amount of vegetables consumed per week after adding kale
    result = veggie_per_week
    return result

print(solution())