def solution():
    total_pages = 45  # The book is 45 pages long
    words_per_page = 200  # Toby averages 200 words per page
    words_per_minute = 300  # Toby can read at a rate of 300 words per minute
    airport_time = 60  # Toby has to be at the airport in 60 minutes

    # Calculate the total number of words Toby has to read
    total_words = total_pages * words_per_page

    # Calculate the time it takes Toby to get to the airport
    airport_time = 10  # It takes 10 minutes to get to the airport

    # Calculate the time it will take Toby early to reach the airport
    early_time = total_words - (total_words * airport_time) - airport_time
    result = early_time
    return result

print(solution())