def solution():
    """Jake is watching a new show, and is worried about how much time he has spent watching it. He spent half the day on Monday watching his show, 4 hours on Tuesday watching his show, a quarter of the day on Wednesday watching his show, and he spent half as much time watching the show on Thursday as he had done in total throughout the previous few days. On Friday, he finally finished watching it. If the entire show is 52 hours long, how many hours did Jake watch on Friday?"""
    # Define the length of the show and the time Jake spent watching it each day
    show_length = 52
    monday_time = 0.5
    tuesday_time = 4
    wednesday_time = 0.25
    thursday_time = 0

    # Calculate the total time Jake spent watching the show from Monday to Wednesday
    total_time = monday_time + tuesday_time + wednesday_time
    
    # Calculate the time Jake spent watching the show on Thursday
    thursday_time = total_time / 2
    
    # Calculate the time Jake spent watching the show on Friday
    friday_time = show_length - total_time - thursday_time
    
    result = friday_time
    return result

print(solution())