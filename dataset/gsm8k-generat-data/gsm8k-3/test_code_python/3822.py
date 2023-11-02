def solution():
    """Alec is running for Class President. He thinks that if he can get three-quarters of the class to vote for him then there is no chance anyone else can beat him. Half of the class have already said they will vote for him but out of the remaining students, only 5 have said they are thinking about voting for him. He surveys the students who are thinking about voting for someone else, and changes his flyers to reflect the issues these students are concerned about. This results in a fifth of these students saying they'll vote for him. If Alec's class has 60 students and everyone who said they will vote for him does so, how many more votes does Alec need to reach his goal number of votes?"""
    # Define the class size
    class_size = 60

    # Define Alec's target percentage
    target_percentage = 0.75

    # Calculate Alec's target number of votes
    target_votes = class_size * target_percentage

    # Calculate the number of students who have already said they will vote for Alec
    initial_support = class_size / 2

    # Calculate the number of additional students who are considering voting for Alec
    additional_support = 5

    # Calculate the number of students who are currently not supporting Alec
    opposition = class_size - initial_support - additional_support

    # Update Alec's flyers to address the concerns of the opposition
    updated_support = opposition / 5

    # Calculate Alec's total support
    total_support = initial_support + additional_support + updated_support

    # Calculate the number of additional votes Alec needs to reach his target
    additional_votes_needed = target_votes - total_support

    # Display the number of additional votes needed
    result = additional_votes_needed
    return result

print(solution())