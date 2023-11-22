def solution():
    
    # Define the number of penpals and the number of letters per penpenpenpenpenpenal
    num_penpals = 5
    num_letters = 2

    # Define the number of pages per penpenpenal and the number of pages per letter
    num_pages_per_letter = 5

    # Calculate the total number of pages written per week
    total_pages_per_week = num_letters * num_pages_per_letter * 7

    # Calculate the total time spent writing per week
    total_time_per_week = total_pages_per_week / 6  # assuming Mike can write a page every 6 minutes

    # Display the total time spent writing per week
    result = total_time_per_week
    return result

print(solution())