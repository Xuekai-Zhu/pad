def solution():
    """A classroom has a whiteboard which is shared between the 4 teachers who take turns using the classroom. Each teacher has 2 lessons per day and uses the whiteboard in each lesson. If the whiteboard is cleaned 3 times per lesson, how many times is the whiteboard cleaned in a day?"""
    teachers = 4
    lessons_per_day = 2
    cleanings_per_lesson = 3
    total_cleanings = teachers * lessons_per_day * cleanings_per_lesson
    result = total_cleanings
    return result

print(solution())