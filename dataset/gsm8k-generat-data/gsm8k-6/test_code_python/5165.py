def solution():
    # Calculate the total number of sentences in the book
    total_sentences = 20 * 10 * 50  # 20 paragraphs per page, 10 sentences per paragraph, 50 pages in the book

    # Calculate the total time Gwendolyn will take to read the book
    time_in_hours = total_sentences / 200  # Gwendolyn can read 200 sentences of a book in 1 hour
    result = time_in_hours
    return result

print(solution())