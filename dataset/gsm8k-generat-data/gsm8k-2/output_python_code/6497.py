def solution():
    """DeShaun always wins the award in English class for reading the most books over the summer. This year is no different. Summer break is 80 days long. When he arrives, he notifies the teacher that he read 60 books over the summer. Each book averaged 320 pages long. The person closest to him read 75% as much as he did. How many pages did the second person read on average each day of break?"""
    total_pages = 60 * 320
    days = 80
    deshaun_pages_per_day = total_pages / days
    second_person_pages = 0.75 * total_pages
    second_person_pages_per_day = second_person_pages / days
    result = second_person_pages_per_day
    return result

print(solution())