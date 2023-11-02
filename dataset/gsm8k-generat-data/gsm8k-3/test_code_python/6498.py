def solution():
    """DeShaun always wins the award in English class for reading the most books over the summer. This year is no different. Summer break is 80 days long. When he arrives, he notifies the teacher that he read 60 books over the summer. Each book averaged 320 pages long. The person closest to him read 75% as much as he did. How many pages did the second person read on average each day of break?"""
    # Define DeShaun's number of books and pages, and the length of summer break
    deshaun_books = 60
    deshaun_pages = 320 * deshaun_books
    break_length = 80

    # Calculate the number of pages the second person read
    second_person_pages = deshaun_pages * 0.75

    # Calculate the average number of pages per day for the second person
    pages_per_day = second_person_pages / break_length

    # Display the average number of pages per day for the second person
    result = pages_per_day
    return result

print(solution())