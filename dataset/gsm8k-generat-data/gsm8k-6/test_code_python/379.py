def solution():
    # Calculate the total cost of buying the piano and hiring the teacher
    piano_cost = 500
    lesson_cost = 20 * 40 * 0.75  # 25% discount on 20 lessons at $40 per lesson
    total_cost = piano_cost + lesson_cost
    result = total_cost
    return result

print(solution())