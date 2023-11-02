def solution():
    """The number of students who wish to go on a skiing trip is twice as many as those who wish to go on a scavenger hunting trip. If there are 4000 students who wish to go on the scavenger hunting trip, how many students are there altogether?"""
    # Define the number of students who want to go on the scavenger hunting trip
    scavenger_hunters = 4000

    # Calculate the number of students who want to go skiing
    skiers = scavenger_hunters * 2

    # Calculate the total number of students
    total_students = scavenger_hunters + skiers

    # Display the total number of students
    result = total_students
    return result

print(solution())