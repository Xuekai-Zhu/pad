def solution():
    """The city of Richmond has 1000 more people than Victoria. Victoria has 4 times as many people as Beacon. If Richmond has 3000 people, how many people are there in Beacon?"""
    # Define the number of people in Richmond and Victoria
    richmond = 3000
    victoria = richmond - 1000

    # Calculate the number of people in Beacon
    beacon = victoria // 4

    # Display the number of people in Beacon
    result = beacon
    return result

print(solution())