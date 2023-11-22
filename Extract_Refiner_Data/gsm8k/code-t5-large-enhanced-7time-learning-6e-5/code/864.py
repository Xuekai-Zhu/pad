def solution():
    
    # Define the number of small jello cups in a box
    BOX_SIZE = 10

    # Define the number of kids Greg wants to have
    NUM_KIDS = 30

    # Define the number of jello cups each kid can have
    JELLO_CUPS_PER_KID = 4

    # Calculate the total number of jello cups needed
    total_jello_cups = NUM_KIDS * JELLO_CUPS_PER_KID

    # Calculate the total cost of the jello
    total_cost = total_jello_cups * 1.25

    # Display the total cost
    result = total_cost
    return result

print(solution())