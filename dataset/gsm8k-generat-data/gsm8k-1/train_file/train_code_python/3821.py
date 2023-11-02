def solution():
    """Alec is running for Class President. He thinks that if he can get three-quarters of the class to vote for him then there is no chance anyone else can beat him. Half of the class have already said they will vote for him but out of the remaining students, only 5 have said they are thinking about voting for him. He surveys the students who are thinking about voting for someone else, and changes his flyers to reflect the issues these students are concerned about. This results in a fifth of these students saying they'll vote for him. If Alec's class has 60 students and everyone who said they will vote for him does so, how many more votes does Alec need to reach his goal number of votes?"""
    class_size = 60
    goal_percent = 0.75
    already_voting_for_him = class_size / 2
    remaining_students = class_size - already_voting_for_him
    possible_additional_votes = remaining_students + 5
    flyers_effect = possible_additional_votes / 5
    total_possible_votes = already_voting_for_him + possible_additional_votes + flyers_effect
    votes_needed = (class_size * goal_percent) - already_voting_for_him
    result = votes_needed
    return result

print(solution())