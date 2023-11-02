def solution():
    """One of the activities in Grade 6 PE class is to get the average weight of the students from each group. In one of the groups, the average weight of five girls is 45 kg while the average weight of five boys is 55 kg. What is the average weight of the ten students from that group?"""
    # Define the number of girls and boys in the group
    num_girls = 5
    num_boys = 5

    # Define the average weight of girls and boys respectively
    girls_weight = 45
    boys_weight = 55

    # Calculate the total weight of all the girls
    total_girls_weight = num_girls * girls_weight

    # Calculate the total weight of all the boys
    total_boys_weight = num_boys * boys_weight

    # Calculate the total weight of all the students
    total_weight = total_girls_weight + total_boys_weight

    # Calculate the average weight of all the students
    average_weight = total_weight / (num_girls + num_boys)

    # Display the average weight of all the students
    result = average_weight
    return result

print(solution())