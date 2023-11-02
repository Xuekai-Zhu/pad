def solution():
    anna_time = 100  # time taken by Anna to read a 100-page book
    carole_speed = 2  # reading speed of Carole (half of Brianna's)
    brianna_pages_per_minute = 2  # Brianna's reading speed (twice of Carole's)
    num_pages = 100

    # Calculate the time taken by Carole to read the book
    carole_time = num_pages * carole_speed

    # Calculate the time taken by Brianna to read the book
    brianna_time = num_pages / brianna_pages_per_minute

    result = brianna_time
    return result

print(solution())