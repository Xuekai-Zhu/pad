def solution():
    """Alec is running for Class President. He thinks that if he can get three-quarters of the class to vote for him then there is no chance anyone else can beat him. Half of the class have already said they will vote for him but out of the remaining students, only 5 have said they are thinking about voting for him. He surveys the students who are thinking about voting for someone else, and changes his flyers to reflect the issues these students are concerned about. This results in a fifth of these students saying they'll vote for him. If Alec's class has 60 students and everyone who said they will vote for him does so, how many more votes does Alec need to reach his goal number of votes?"""
    total_students = 60
    vote_goal = 0.75 * total_students
    initial_votes = 0.5 * total_students + 5
    changed_flyers_votes = (1/5) * (total_students - initial_votes)
    total_votes = initial_votes + changed_flyers_votes
    additional_votes_needed = vote_goal - total_votes
    result = additional_votes_needed
    return result

print(solution())