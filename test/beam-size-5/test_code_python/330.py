def solution():
    
    # Define the number of guns each person has
    dj_gns = 8
    nick_gns = 10
    richard_gns = 5

    # Calculate the total number of guns
    total_gns = dj_gns + nick_gns + richard_gns

    # Calculate the number of guns each person would have if they share equally
    each_person_gns = total_gns // 3

    # Display the number of guns each person would have
    result = each_person_gns
    return result

print(solution())