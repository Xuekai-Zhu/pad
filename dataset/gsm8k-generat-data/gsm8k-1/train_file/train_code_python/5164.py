def solution():
    """Gwendolyn can read 200 sentences of a book in 1 hour. She just brought a book from the library, having 20 paragraphs per page. What's the total time Gwendolyn will take to read the book if each paragraph has 10 sentences and the book has 50 pages?"""
    sentences_per_hour = 200
    paragraphs_per_page = 20
    sentences_per_paragraph = 10
    pages = 50
    total_sentences = paragraphs_per_page * sentences_per_paragraph * pages
    total_time_in_hours = total_sentences / sentences_per_hour
    result = total_time_in_hours
    return result

print(solution())