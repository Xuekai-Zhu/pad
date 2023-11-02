def solution():
    sentences_per_hour = 200
    sentences_per_paragraph = 10
    paragraphs_per_page = 20
    pages_in_book = 50
    total_sentences = sentences_per_paragraph * paragraphs_per_page * pages_in_book
    total_time = total_sentences / sentences_per_hour
    result = total_time
    return result

print(solution())