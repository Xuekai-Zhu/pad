def solution():
    """Ellis is going to take a road trip with her family. First, she needs to figure out how many bottles of water she should bring for everyone. There will be four people total: Ellis, her mother, her sister, and her aunt. They will be on the road to their destination for 8 hours and drive 8 hours to return home. Every hour each person will want to drink 1/2 a bottle of water. How many water bottles will Ellis' family need total?"""
    # Define the number of people and hours
    num_people = 4
    num_hours = 16  # 8 hours to the destination and 8 hours returning

    # Calculate the total number of water bottles needed
    total_bottles = num_people * 0.5 * num_hours

    # Display the total number of water bottles needed
    result = total_bottles
    return result

print(solution())