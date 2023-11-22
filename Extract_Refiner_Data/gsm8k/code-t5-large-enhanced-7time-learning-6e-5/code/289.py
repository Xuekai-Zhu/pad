def solution():
    
    # Define the number of points Mike has
    mike_points = 21

    # Calculate the number of points Jim has
    jim_points = mike_points - 3

    # Calculate the number of points Tony has
    tony_points = mike_points * 2

    # Calculate the total points before the extra points were distributed
    total_points = mike_points + jim_points + tony_points

    # Calculate the number of points over the fourth round
    over_points = total_points - 20

    # Calculate the total points after the extra points were distributed
    total_points += over_points

    # Display the total points
    result = total_points
    return result

print(solution())