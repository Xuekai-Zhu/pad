def solution():
    sentences_per_hour = 200
    paragraphs_per_page = 20
    sentences_per_paragraph = 10
    num_pages = 50

    # Calculate the total number of paragraphs in the book
    total_paragraphs = paragraphs_per_page * num_pages

    # Calculate the total number of sentences in the book
    total_sentences = total_paragraphs * sentences_per_paragraph

    # Calculate the total time it will take Gwendolyn to read the book
    total_time = total_sentences / sentences_per_hour  # in hours
    result = total_time
    return result

print(solution())