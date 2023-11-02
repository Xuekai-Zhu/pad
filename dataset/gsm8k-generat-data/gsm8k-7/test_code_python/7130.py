def solution():
    initial_people = 0 # initialize the counter for the number of people at the start of Bethany's shift
    final_people = 19 # given that there are now 19 people in the gym
    running_people = 5 # given that 5 more people came in and started running on the treadmill
    leaving_people = 2 # given that 2 people left
    initial_people = final_people - running_people + leaving_people # calculate the number of people at the start of Bethany's shift
    result = initial_people
    return result

print(solution())