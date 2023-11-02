def solution():
    """Vicki is planning a pop concert at her high school. The show will be 2 hours. She is allowing each group 2 minutes to get on stage, 6 minutes to perform, and then 2 minutes to exit the stage. If she allows a 10-minute intermission, how many groups can perform in the concert?"""
    total_time = 2 * 60 # in minutes
    time_per_group = 2 + 6 + 2 # in minutes
    intermission_time = 10 # in minutes
    time_per_set = time_per_group * 4 + intermission_time # each set has 4 performances and one intermission
    groups_per_set = 4 # there are 4 performances per set
    total_groups = (total_time // time_per_set) * groups_per_set # integer division to get the number of sets, multiply by groups per set
    result = total_groups
    return result

print(solution())