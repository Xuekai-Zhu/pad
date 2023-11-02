def solution():
    """At a roller derby, 4 teams are competing. Each team is made up of 10 members,
    and each member needs a pair of roller skates to compete in and another pair of skates as a backup.
    None of the skates have laces yet, so each member is offered 3 sets of laces per pair of skates.
    How many sets of laces have been handed out?"""
    # Define the number of teams and members per team
    NUM_TEAMS = 4
    MEMBERS_PER_TEAM = 10

    # Calculate the total number of members
    total_members = NUM_TEAMS * MEMBERS_PER_TEAM

    # Calculate the total number of pairs of skates needed
    total_skates = total_members * 2

    # Calculate the total number of sets of laces needed
    total_laces = total_skates * 3

    # Display the total number of sets of laces
    result = total_laces
    return result

print(solution())