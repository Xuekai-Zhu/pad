def solution():
    """Mandy started reading books with only 8 pages when she was 6 years old. By the time she was twice that age, she was reading books 5 times longer, and 8 years later, she was reading books 3 times longer than that. Presently, she reads books that are 4 times the previous length. How many pages do the books she reads now have?"""
    starting_age = 6
    starting_length = 8
    twice_age = starting_age * 2
    twice_length = starting_length * 5
    later_age = twice_age + 8
    later_length = twice_length * 3
    current_length = later_length * 4
    result = current_length
    return result

print(solution())