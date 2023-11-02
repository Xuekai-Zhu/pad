def solution():
    """A group of 300 athletes spent Saturday night at Ultimate Fitness Camp. The next morning, for 4 hours straight, they left the camp at a rate of 28 athletes per hour. Over the next 7 hours, a new group of athletes trickled into the camp at a rate of 15 athletes per hour. Immediately thereafter, the camp gate was shut and everyone went to bed. What is the difference in the total number of athletes in the camp over the two nights?"""
    initial_number_of_athletes = 300
    athletes_leaving_camp_per_hour = 28
    athletes_arriving_per_hour = 15
    total_number_of_athletes_leaving = athletes_leaving_camp_per_hour * 4
    total_number_of_athletes_arriving = athletes_arriving_per_hour * 7
    total_number_of_athletes_on_Sunday = initial_number_of_athletes - total_number_of_athletes_leaving + total_number_of_athletes_arriving
    difference_in_total_number_of_athletes = total_number_of_athletes_on_Sunday - initial_number_of_athletes
    result = difference_in_total_number_of_athletes
    return result

print(solution())