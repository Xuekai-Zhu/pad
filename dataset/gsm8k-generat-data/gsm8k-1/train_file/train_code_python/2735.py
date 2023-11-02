def solution():
    """Paul lives in a 5th story apartment. He makes 3 trips out from and back to his apartment throughout the day each day of a week. How many feet does he travel vertically in total over the week if each story is 10 feet tall?"""
    num_trips = 3
    num_days = 7
    num_stories = 5
    story_height = 10
    total_distance = num_trips * num_days * num_stories * story_height * 2
    result = total_distance
    return result

print(solution())