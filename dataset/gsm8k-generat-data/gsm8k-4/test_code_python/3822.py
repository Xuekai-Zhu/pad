def solution():
    """Alec is running for Class President. He thinks that if he can get three-quarters of the class to vote for him then there is no chance anyone else can beat him. Half of the class have already said they will vote for him but out of the remaining students, only 5 have said they are thinking about voting for him. He surveys the students who are thinking about voting for someone else, and changes his flyers to reflect the issues these students are concerned about. This results in a fifth of these students saying they'll vote for him. If Alec's class has 60 students and everyone who said they will vote for him does so, how many more votes does Alec need to reach his goal number of votes?"""
    # Define the total number of students in the class
    total_students = 60

    # Calculate the number of students who have already said they will vote for Alec
    initial_supporters = total_students * 0.5

    # Calculate the number of students who are considering voting for Alec
    potential_supporters = total_students - initial_supporters - 5

    # Calculate the number of students who are not considering voting for Alec
    non_supporters = total_students - initial_supporters - potential_supporters

    # Calculate the number of potential supporters who were swayed by Alec's new flyers
    new_supporters = potential_supporters * 0.2

    # Calculate the total number of supporters Alec has
    total_supporters = initial_supporters + new_supporters

    # Calculate the number of votes Alec needs to reach his goal
    goal_votes = total_students * 0.75
    remaining_votes = goal_votes - total_supporters

    # Return the number of additional votes Alec needs
    result = remaining_votes
    return result

print(solution())