def solution():
    """Nina has four times more math homework and eight times more reading homework than Ruby. If Ruby has six math homework and two reading homework, how much homework is Nina having altogether?"""
    ruby_math = 6
    ruby_reading = 2
    nina_math = 4 * ruby_math
    nina_reading = 8 * ruby_reading
    total_homework = nina_math + nina_reading
    result = total_homework
    return result

print(solution())