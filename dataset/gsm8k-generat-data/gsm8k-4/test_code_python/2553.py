def solution():
    """Connor sleeps 6 hours a night. His older brother Luke sleeps 2 hours longer than Connor. Connor’s new puppy sleeps twice as long as Luke. How long does the puppy sleep?"""
    # Define the length of time Connor sleeps
    connor_sleep = 6

    # Define the length of time Luke sleeps, based on Connor's sleep
    luke_sleep = connor_sleep + 2

    # Define the length of time the puppy sleeps, based on Luke's sleep
    puppy_sleep = luke_sleep * 2

    result = puppy_sleep
    return result

print(solution())