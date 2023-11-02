def solution():
    """It takes 1 person working 10 hours to figure out the solution to a math problem. If you add a second person who's equally good at math, how long will the two of them have to work to solve the same problem?"""
    hours_per_person = 10
    number_of_people = 2
    total_hours = hours_per_person / number_of_people
    result = total_hours
    return result

print(solution())