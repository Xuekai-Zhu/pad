def solution():
    
    # Define the number of members in the Reddit group
    members = 1000

    # Define the average number of posts per member per day
    posts_per_member_per_day = 3

    # Calculate the total number of posts in March
    total_posts = members * posts_per_member_per_day * 365

    # Display the total number of posts in March
    result = total_posts
    return result

print(solution())