def solution():
    """Each week Carina puts 20 more seashells in a jar than she did the week before. If there are 50 seashells in the jar this week, how many will there be in a month?"""
    # Define the initial number of seashells and the increase each week
    initial_seashells = 50
    increase_per_week = 20

    # Calculate the number of seashells in the jar after one month (4 weeks)
    seashells_in_a_month = initial_seashells + increase_per_week * 3

    # Display the number of seashells in a month
    result = seashells_in_a_month
    return result

print(solution())