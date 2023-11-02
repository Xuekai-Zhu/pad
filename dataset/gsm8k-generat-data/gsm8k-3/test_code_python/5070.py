def solution():
    """While reading in bed with his wife Susan, Charlie heard a noise at the door. It was Sarah entering the bedroom with 4 friends. If there were also 8 people in the living room, how many people are in the house?"""
    # Define the initial number of people in the house
    initial_num_people = 2 # Charlie and Susan

    # Add the number of people Sarah brought in
    num_people = initial_num_people + 4

    # Add the number of people in the living room
    num_people += 8

    # Display the total number of people in the house
    result = num_people
    return result

print(solution())