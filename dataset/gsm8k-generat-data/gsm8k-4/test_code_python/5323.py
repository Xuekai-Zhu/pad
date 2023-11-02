def solution():
    """Tom and Elizabeth have a competition to climb a hill. Elizabeth takes 30 minutes to climb the hill. Tom takes four times as long as Elizabeth does to climb the hill. How many hours does it take Tom to climb up the hill?"""
    # Define Elizabeth's climbing time in minutes
    elizabeth_time = 30

    # Define Tom's climbing time as a multiple of Elizabeth's
    tom_multiple = 4
    tom_time = elizabeth_time * tom_multiple

    # Convert Tom's climbing time to hours
    tom_hours = tom_time / 60

    result = tom_hours
    return result

print(solution())