def solution():
    """Cindy's math and science books weigh 2 pounds each. Her French book weighs 4 pounds and her English book weighs 3 pounds. Her history book weighs twice as much as her English book. If Cindy carries all of her books at once, what will be the total weight of the books she is carrying?"""
    math_science_books_weight = 2 * 2
    french_book_weight = 4
    english_book_weight = 3
    history_book_weight = 2 * english_book_weight
    total_weight = math_science_books_weight + french_book_weight + english_book_weight + history_book_weight
    result = total_weight
    return result

def solution():
    """Samantha's last name has three fewer letters than Bobbie's last name. If Bobbie took two letters off her last name, she would have a last name twice the length of Jamie's. Jamie's full name is Jamie Grey. How many letters are in Samantha's last name?"""
    jamie_full_name_length = len("Jamie Grey")
    bobbie_last_name_length = (jamie_full_name_length * 2) + 2
    samantha_last_name_length = bobbie_last_name_length - 3
    result = samantha_last_name_length
    return result

print(solution())