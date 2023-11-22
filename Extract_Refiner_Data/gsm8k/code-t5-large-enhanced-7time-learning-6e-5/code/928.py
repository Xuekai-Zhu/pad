def solution():
    
    # Define the number of friends Maria invited over
    num_friends = 4

    # Define the number of water balloons Maria gave each friend
    friend_balloons = 2

    # Define the number of water balloons Maria had before herself
    initial_balloons = 1

    # Define the number of water balloons Maria's mom gave each person
    mom_balloons = 3

    # Calculate the total number of water balloons Maria gave away
    total_given_away = num_friends * friend_balloons

    # Calculate the total number of water balloons Maria's girls had after her mom gave some
    total_given_away += mom_balloons

    # Calculate the total number of water balloons the girls had
    total_balloons = initial_balloons + total_given_away

    # Display the total number of water balloons

print(solution())