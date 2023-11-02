def solution():
    lesson_time = 1  # Caprice takes 1 hour lesson every week
    cost_per_half_hour = 10  # The teacher charges $10 for every half hour of teaching
    lessons_per_week = 1  # Caprice takes 1 lesson per week
    weeks = 5  # Caprice wants to know the teacher's earnings in 5 weeks

    # Calculate the total earnings of the teacher in 5 weeks
    total_earnings = cost_per_half_hour * lesson_time * 2 * lessons_per_week * weeks

    result = total_earnings
    return result

print(solution())