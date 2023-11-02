def solution():
    """The lunchroom is full of students: 40% are girls and the remainder are boys. There are 2 monitors for every 15 students. There are 8 monitors. Every boy drinks, on average, 1 carton of milk, and every girl drinks, on average, 2 cartons of milk. How many total cartons of milk are consumed by the students in the lunchroom?"""
    # Define the proportion of girls in the lunchroom
    GIRLS_PROPORTION = 0.4

    # Calculate the number of students in the lunchroom
    total_students = (8 / 2) * 15

    # Calculate the number of girls and boys in the lunchroom
    girls = int(total_students * GIRLS_PROPORTION)
    boys = total_students - girls

    # Calculate the total number of cartons of milk consumed
    total_milk = (girls * 2) + (boys * 1)

    # Display the total number of cartons of milk consumed
    result = total_milk
    return result

print(solution())