def solution():
    """The school is organizing a trip to the museum. 4 buses were hired to take the children and teachers to their destination. The second bus has twice the number of people on it as the first bus. The third bus has 6 fewer people than the second bus. The fourth bus has 9 more people than the first bus. If the first bus has 12 people, how many people are going to the museum in total?"""
    first_bus = 12
    second_bus = 2 * first_bus
    third_bus = second_bus - 6
    fourth_bus = first_bus + 9
    total_people = first_bus + second_bus + third_bus + fourth_bus
    result = total_people
    return result

print(solution())