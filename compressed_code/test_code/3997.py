def solution():
    
    sentences_per_hour = 200
    paragraphs_per_page = 20
    sentences_per_paragraph = 10
    total_sentences = paragraphs_per_page * sentences_per_paragraph * 50
    total_hours = total_sentences / sentences_per_hour
    result = total_hours
    return result

print(solution())