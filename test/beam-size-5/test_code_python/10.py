def solution():
    
    # Define the total number of students in the class
    total_students = 20

    # Calculate the number of enrolled in contemporary dance
    contemporary_ enrolled = total_students * 0.2

    # Calculate the number of remaining enrolled in dance
    remaining_ enrolled = total_students - contemporary_ enrolled

    # Calculate the number of enrolled in jazz dance
    jazz_ enrolled = remaining_ enrolled * 0.25

    # Calculate the number of enrolled in hip-hop dance
    hiphop_ enrolled = total_students - contemporary_ enrolled - jazz_ enrolled

    # Calculate the percentage of enrolled in hip-hop dance
    hiphop_percentage = (hiphop_ enrolled / total_students) * 100

    # Display the percentage of enrolled in hip-hop dance
    result = hiphop_percentage
    return result

print(solution())