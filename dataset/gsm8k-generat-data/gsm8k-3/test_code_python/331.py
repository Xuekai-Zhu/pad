def solution():
    """Samuel bought 2 dozen doughnuts and Cathy bought 3 dozen doughnuts. They planned to share the doughnuts evenly with their 8 other friends. How many doughnuts will each of them receive?"""
    # Define the number of dozens of doughnuts each person bought
    samuel_dozens = 2
    cathy_dozens = 3

    # Calculate the total number of dozens of doughnuts
    total_dozens = samuel_dozens + cathy_dozens

    # Calculate the total number of doughnuts
    total_doughnuts = total_dozens * 12

    # Calculate the number of doughnuts each person will receive
    num_people = 10  # Samuel, Cathy, and 8 friends
    doughnuts_per_person = total_doughnuts / num_people

    # Display the number of doughnuts each person will receive
    result = doughnuts_per_person
    return result

print(solution())