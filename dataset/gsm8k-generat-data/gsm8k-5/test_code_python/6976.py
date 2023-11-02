def solution():
    current_seashells = 50  # There are 50 seashells in the jar this week
    added_seashells = 20  # Carina puts 20 more seashells in the jar each week
    weeks_in_month = 4  # There are 4 weeks in a month

    # Calculate the total number of seashells added in a month
    total_added_seashells = (current_seashells + (current_seashells + added_seashells) + (current_seashells + 2*added_seashells) + (current_seashells + 3*added_seashells))

    # Calculate the total number of seashells in the jar after a month
    total_seashells = current_seashells + total_added_seashells
    result = total_seashells
    return result

print(solution())