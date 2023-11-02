def solution():
    """Gwendolyn can read 200 sentences of a book in 1 hour. She just brought a book from the library, having 20 paragraphs per page. What's the total time Gwendolyn will take to read the book if each paragraph has 10 sentences and the book has 50 pages?"""
    # Define the number of sentences per hour
    sentences_per_hour = 200

    # Define the number of paragraphs per page and the number of sentences per paragraph
    paragraphs_per_page = 20
    sentences_per_paragraph = 10

    # Define the number of pages in the book
    num_pages = 50

    # Calculate the total number of sentences in the book
    num_sentences = num_pages * paragraphs_per_page * sentences_per_paragraph

    # Calculate the total time it will take Gwendolyn to read the book
    time_hours = num_sentences / sentences_per_hour

    result = time_hours
    return result

print(solution())