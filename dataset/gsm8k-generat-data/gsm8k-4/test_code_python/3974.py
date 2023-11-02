def solution():
    """John reads his bible every day. He reads for 2 hours a day and reads at a rate of 50 pages an hour. If the bible is 2800 pages long how many weeks will it take him to read it all?"""
    # Define the number of pages in the bible and John's reading rate
    bible_pages = 2800
    reading_rate = 50 * 2  # pages per day

    # Calculate the number of days it will take to finish the bible
    days = bible_pages / reading_rate

    # Convert the number of days to weeks
    weeks = days / 7

    # Round up to the nearest integer
    weeks = int(weeks) + 1

    return weeks

print(solution())