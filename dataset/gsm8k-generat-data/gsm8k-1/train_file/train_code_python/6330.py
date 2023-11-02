def solution():
    """Anna can read 1 page in 1 minute. Carole can read as fast as Anna but at half the speed of Brianna. How long does it take Brianna to read a 100-page book?"""
    anna_time = 100 # Anna can read 100 pages in 100 minutes
    carole_speed = 2 # Carole reads at half Brianna's speed, so it takes her 2 minutes to read 1 page
    brianna_time = carole_speed # Brianna reads at double Carole's speed, so it takes her 1 minute to read 1 page
    time_to_read_book = 100 * brianna_time # Brianna takes 1 minute to read 1 page, so it will take her 100 minutes to read a 100-page book
    result = time_to_read_book
    return result

print(solution())