def solution():
    """Caprice is taking piano lessons. Her mother pays the teacher $10 for every half-hour of teaching her daughter. If Caprice is taking one lesson per week, and the lesson lasts 1 hour, how much money would the teacher earn in 5 weeks?"""
    lesson_length = 1 # hour
    lesson_frequency = 1 # per week
    cost_per_half_hour = 10
    total_cost_per_lesson = cost_per_half_hour * 2 * lesson_length
    total_lessons = 5
    total_cost = total_cost_per_lesson * total_lessons * lesson_frequency
    
    result = total_cost
    return result

print(solution())