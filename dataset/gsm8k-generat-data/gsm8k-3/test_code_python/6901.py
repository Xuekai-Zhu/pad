def solution():
    """Ron ate pizza with his friends the other day. If they ordered a 12-slice pizza and each of them ate 4 slices, how many friends were there with Ron?"""
    # Define the total number of slices and the number of slices each person ate
    total_slices = 12
    slices_per_person = 4

    # Calculate the number of people who ate pizza with Ron
    num_friends = total_slices // slices_per_person

    # Display the number of friends
    result = num_friends
    return result

print(solution())