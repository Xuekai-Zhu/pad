def solution():
    """Kimiko watches four YouTube videos. The first video is 2 minutes long, the second video is 4 minutes and 30 seconds, and the last two videos are equal in length. If she spends a total of 510 seconds watching YouTube, how many seconds long was each of the last two videos?"""
    # Define the lengths of the first two videos in seconds
    video1_length = 2 * 60
    video2_length = 4 * 60 + 30

    # Calculate the total length of the first two videos
    first_two_length = video1_length + video2_length 

    # Calculate the length of each of the last two videos
    last_two_length = (510 - first_two_length) / 2

    # Display the result
    result = last_two_length
    return result

print(solution())