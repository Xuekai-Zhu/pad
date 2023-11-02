def solution():
    """Mandy started reading books with only 8 pages when she was 6 years old. By the time she was twice that age, she was reading books 5 times longer, and 8 years later, she was reading books 3 times longer than that. Presently, she reads books that are 4 times the previous length. How many pages do the books she reads now have?"""
    starting_age = 6
    starting_length = 8

    # Book lengths at different stages
    double_age = 2 * starting_age
    double_age_length = 5 * starting_length
    eight_years_later_length = 3 * double_age_length
    current_length = 4 * eight_years_later_length

    result = current_length
    return result

print(solution())