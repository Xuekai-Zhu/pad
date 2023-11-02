def solution():
    
    # Define the number of members in the group and the average number of posts per day
    members = 1000
    posts_per_day = 3

    # Calculate the total number of posts in March
    total_posts = members * posts_per_day * 7

    # Display the total number of posts
    result = total_posts
    return result

print(solution())