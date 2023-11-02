def solution():
    """Yasna has two books. One book is 180 pages long, and the other book is 100 pages long. If Yasna wants to finish both of the books in two weeks, how many pages will Yasna need to read every day, if she reads an equal number of pages each day?"""
    # Define the total number of pages to read
    total_pages = 180 + 100

    # Define the number of days Yasna has to read the books
    num_days = 14

    # Calculate the number of pages Yasna needs to read per day
    pages_per_day = total_pages / num_days

    # Display the number of pages Yasna needs to read per day
    result = pages_per_day
    return result

print(solution())