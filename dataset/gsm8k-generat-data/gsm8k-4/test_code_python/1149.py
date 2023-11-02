def solution():
    """Mandy started reading books with only 8 pages when she was 6 years old. By the time she was twice that age, she was reading books 5 times longer, and 8 years later, she was reading books 3 times longer than that. Presently, she reads books that are 4 times the previous length. How many pages do the books she reads now have?"""
    # Define the initial number of pages and Mandy's age
    pages = 8
    age = 6

    # Calculate the number of pages when Mandy was twice her initial age
    pages *= 5
    age *= 2

    # Calculate the number of pages 8 years after Mandy was twice her initial age
    pages *= 3
    age += 8

    # Calculate the number of pages Mandy reads now
    pages *= 4

    # Display the result
    result = pages
    return result

print(solution())