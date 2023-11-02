def solution():
    """Omar buys a 12-ounce cup of coffee every morning on the way to work. On the way to work, he drinks one-quarter of the cup. When he gets to his office, he drinks another half of the cup. He forgets to drink any more of his coffee once he starts working, and when he remembers his coffee, he only drinks 1 ounce of the remaining amount because it is cold. How many ounces will be left in the cup afterward?"""
    # Define the initial volume of coffee
    volume = 12

    # Calculate the volume Omar drinks on the way to work
    volume -= volume / 4

    # Calculate the volume Omar drinks when he gets to the office
    volume -= volume / 2

    # Calculate the volume Omar drinks later, when he remembers
    volume -= 1

    # Display the remaining volume of coffee
    result = volume
    return result

print(solution())