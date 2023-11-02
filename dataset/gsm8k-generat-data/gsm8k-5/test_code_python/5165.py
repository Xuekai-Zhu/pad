def solution():
    sentences_per_page = 20 * 10  # 20 paragraphs per page, with 10 sentences per paragraph
    total_sentences = sentences_per_page * 50  # The book has 50 pages in total
    sentences_per_hour = 200  # Gwendolyn can read 200 sentences in 1 hour

    # Calculate the total time Gwendolyn will take to read the book
    total_time = total_sentences / sentences_per_hour
    result = total_time
    return result

print(solution())