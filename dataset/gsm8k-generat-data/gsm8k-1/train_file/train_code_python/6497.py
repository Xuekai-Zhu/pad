def solution():
    """DeShaun always wins the award in English class for reading the most books over the summer. This year is no different. Summer break is 80 days long. When he arrives, he notifies the teacher that he read 60 books over the summer. Each book averaged 320 pages long. The person closest to him read 75% as much as he did. How many pages did the second person read on average each day of break?"""
    num_books = 60
    avg_pages_per_book = 320
    total_pages_read = num_books * avg_pages_per_book
    days_of_break = 80
    deshaun_avg_pages_per_day = total_pages_read / days_of_break
    second_person_pct_of_deshaun = 0.75
    second_person_total_pages_read = total_pages_read * second_person_pct_of_deshaun
    second_person_avg_pages_per_day = second_person_total_pages_read / days_of_break
    result = second_person_avg_pages_per_day
    return result

print(solution())