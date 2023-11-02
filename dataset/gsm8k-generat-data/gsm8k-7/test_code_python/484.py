def solution():
    total_people = 25
    people_quit = 8
    new_people = 13

    # Calculate the new total number of people on the team
    new_total_people = total_people - people_quit + new_people
    result = new_total_people
    return result

print(solution())