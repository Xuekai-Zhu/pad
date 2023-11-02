def solution():
    """Lisa is part of a choir that has 52 members, 50% of which are boys and 50% of which are girls. The choir decides to perform with just its female members. On the day of the performance, however, half the people performing can't make it to the show because their bus breaks down. The choir's 3 teachers then decide to sing with them. How many people sang in the performance?"""
    total_members = 52
    girls = total_members / 2
    boys = total_members / 2
    female_members = girls
    female_members_present = female_members / 2
    teachers = 3
    total_singers = female_members_present + teachers
    result = total_singers
    
    return result

print(solution())