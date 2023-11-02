def solution():
    # Define the difference and sum of ages
    age_difference = 2
    total_age = 74

    # Use algebra to solve for the ages of the friends
    # Let x be the age of the younger friend
    # Then x + age_difference = age of the older friend
    # And x + (x + age_difference) = total_age
    # Simplifying, we get 2x + age_difference = total_age
    # Solving for x, we get x = (total_age - age_difference) / 2
    x = (total_age - age_difference) / 2

    # Calculate the age of the older friend
    older_friend_age = x + age_difference
    result = older_friend_age
    return result

print(solution())