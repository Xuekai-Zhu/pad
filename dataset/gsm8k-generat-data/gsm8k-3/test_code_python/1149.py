def solution():
    """Mandy started reading books with only 8 pages when she was 6 years old. By the time she was twice that age, she was reading books 5 times longer, and 8 years later, she was reading books 3 times longer than that. Presently, she reads books that are 4 times the previous length. How many pages do the books she reads now have?"""
    # Define Mandy's age when she started reading books with 8 pages
    age_1 = 6

    # Define Mandy's age when she started reading books 5 times longer
    age_2 = age_1 * 2
    length_2 = 8 * 5

    # Define Mandy's age when she started reading books 3 times longer than the previous ones
    age_3 = age_2 + 8
    length_3 = length_2 * 3

    # Define Mandy's current age and the length of the books she currently reads
    age_now = age_3 + 8
    length_now = length_3 * 4

    # Display the number of pages in the current books Mandy reads
    result = length_now
    return result

print(solution())