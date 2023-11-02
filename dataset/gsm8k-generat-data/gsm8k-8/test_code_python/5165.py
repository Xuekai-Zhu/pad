def solution():
    # Define the given values
    sentences_per_hour = 200
    paragraphs_per_page = 20
    sentences_per_paragraph = 10
    num_pages = 50

    # Calculate the total number of sentences in the book
    total_sentences = paragraphs_per_page * sentences_per_paragraph * num_pages

    # Calculate the time it will take Gwendolyn to read the book
    time_in_hours = total_sentences / sentences_per_hour

    result = time_in_hours
    return result

print(solution())