def solution():
    """Half of all the people in Nantucket will attend a planned meeting for a bowl game. There are 300 people in Nantucket, and the number of males going to the meeting is twice the number of females. How many females are going to the meeting?"""
    # Define the total number of people in Nantucket and the proportion going to the meeting
    total_people = 300
    proportion_attending = 0.5

    # Calculate the number of people attending the meeting
    num_attending = int(total_people * proportion_attending)

    # Calculate the number of males attending the meeting
    num_males = num_attending // 3

    # Calculate the number of females attending the meeting
    num_females = (num_attending - num_males)

    # Display the number of females attending the meeting
    result = num_females
    return result

print(solution())