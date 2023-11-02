def solution():
    """Ellis is going to take a road trip with her family. First, she needs to figure out how many bottles of water she should bring for everyone. There will be four people total: Ellis, her mother, her sister, and her aunt. They will be on the road to their destination for 8 hours and drive 8 hours to return home. Every hour each person will want to drink 1/2 a bottle of water. How many water bottles will Ellis' family need total?"""

    # Define the number of people and the number of hours they will be on the road
    PEOPLE = 4
    HOURS_ON_ROAD = 16

    # Calculate the total number of bottles they will need
    bottles_per_person_per_hour = 0.5
    total_bottles_needed = PEOPLE * HOURS_ON_ROAD * bottles_per_person_per_hour

    result = total_bottles_needed
    return result

print(solution())