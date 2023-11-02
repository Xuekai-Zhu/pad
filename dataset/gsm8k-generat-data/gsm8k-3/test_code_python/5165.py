def solution():
    """Gwendolyn can read 200 sentences of a book in 1 hour. She just brought a book from the library, having 20 paragraphs per page. What's the total time Gwendolyn will take to read the book if each paragraph has 10 sentences and the book has 50 pages?"""
    # Define the number of sentences per hour that Gwendolyn can read
    SENTENCES_PER_HOUR = 200

    # Define the number of paragraphs per page and the number of sentences per paragraph
    PARAGRAPHS_PER_PAGE = 20
    SENTENCES_PER_PARAGRAPH = 10

    # Define the number of pages in the book
    pages = 50

    # Calculate the total number of sentences in the book
    total_sentences = pages * PARAGRAPHS_PER_PAGE * SENTENCES_PER_PARAGRAPH

    # Calculate the total time Gwendolyn will take to read the book
    total_time = total_sentences / SENTENCES_PER_HOUR

    # Display the total time
    result = total_time
    return result

print(solution())