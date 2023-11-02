def solution():
    initial_likes = 2000  # Fishio received 2000 likes on the photo after 1 week
    new_likes = 70 * initial_likes  # Fishio received 70 times as many likes as the initial number of likes
    total_likes = initial_likes + new_likes  # Calculate the total number of likes after three weeks
    result = total_likes
    return result

print(solution())