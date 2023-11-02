def solution():
    """A group of 300 athletes spent Saturday night at Ultimate Fitness Camp. The next morning, for 4 hours straight, they left the camp at a rate of 28 athletes per hour. Over the next 7 hours, a new group of athletes trickled into the camp at a rate of 15 athletes per hour. Immediately thereafter, the camp gate was shut and everyone went to bed. What is the difference in the total number of athletes in the camp over the two nights?"""
    initial_number = 300
    leaving_rate = 28
    leaving_time = 4
    leaving_number = leaving_rate * leaving_time
    arriving_rate = 15
    arriving_time = 7
    arriving_number = arriving_rate * arriving_time
    final_number = initial_number - leaving_number + arriving_number
    difference = final_number - initial_number
    result = difference
    return result

print(solution())