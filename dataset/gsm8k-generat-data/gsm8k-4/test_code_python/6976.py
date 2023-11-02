def solution():
    """Each week Carina puts 20 more seashells in a jar than she did the week before. If there are 50 seashells in the jar this week, how many will there be in a month?"""
    # Define the initial number of seashells and the number of weeks in a month
    initial_seashells = 50
    weeks_in_month = 4

    # Initialize the total seashell count and the increment value
    total_seashells = initial_seashells
    increment = 20

    # Add the increment value each week for four weeks
    for i in range(1, weeks_in_month):
        total_seashells += (initial_seashells + (i * increment))

    # Return the total seashell count
    result = total_seashells
    return result

print(solution())