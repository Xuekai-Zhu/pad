def solution():
    lessons_per_hour = 1 / 1.5  # Michael takes 1 lesson in 1.5 hours, so he takes 2/3 lessons in 1 hour
    lesson_cost = 30  # The cost of one lesson is $30
    total_hours = 18  # Michael wants to take 18 hours of lessons

    # Calculate the total cost of 18 hours of lessons
    total_cost = lessons_per_hour * lesson_cost * total_hours
    result = total_cost
    return result

print(solution())