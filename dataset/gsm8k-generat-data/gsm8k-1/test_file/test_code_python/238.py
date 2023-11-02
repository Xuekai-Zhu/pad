I'm sorry, I cannot solve the Samantha's last name problem as it requires additional information.

def solution():
    """Mike was a pen pal with 5 people. He stopped being penpals with 2 of them. They each send 2 letters a week that are 5 pages long. He responds in kind. He can write a page every 6 minutes. How many hours does he spend writing a week?"""
    num_penpals = 5
    num_penpals -= 2
    num_letters_sent = 2
    pages_per_letter = 5
    total_pages_sent = num_penpals * num_letters_sent * pages_per_letter
    time_to_write_one_page_min = 6
    time_to_write_one_page_hr = time_to_write_one_page_min / 60
    total_time_spent_writing_hr = total_pages_sent * time_to_write_one_page_hr
    result = total_time_spent_writing_hr
    return result

print(solution())