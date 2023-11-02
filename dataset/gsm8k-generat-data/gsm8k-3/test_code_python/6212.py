def solution():
    """Daragh had 20 stuffed bears. She took out her favorite 8 bears and then equally divided the other bears among her 3 sisters. Daragh's youngest sister, Eden, already had 10 stuffed bears. How many stuffed bears does Eden have now?"""
    # Define the number of bears Daragh had initially
    initial_bears = 20

    # Define the number of Daragh's favorite bears
    favorite_bears = 8

    # Calculate the number of bears Daragh has left to distribute
    remaining_bears = initial_bears - favorite_bears

    # Divide the remaining bears equally among Daragh's 3 sisters
    sisters_bears = remaining_bears / 3

    # Calculate the total number of bears Eden has now
    eden_bears = sisters_bears + 10

    # Display the number of stuffed bears Eden has now
    result = eden_bears
    return result

print(solution())