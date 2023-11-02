def solution():
    
    sentences_per_hour = 200
    paragraphs_per_page = 20
    sentences_per_paragraph = 10
    pages = 50
    total_sentences = paragraphs_per_page * sentences_per_paragraph * pages
    total_time_in_hours = total_sentences / sentences_per_hour
    result = total_time_in_hours
    return result

print(solution())