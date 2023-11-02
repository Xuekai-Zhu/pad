def solution():
    """Pat is buying supplies for S'mores. He and his friends will each eat 3 S'mores. There are 8 of them in total. It costs $3 in supplies to make 4 S'mores. How much will it cost to buy all the supplies?"""
    # Define the number of S'mores each person will eat and the number of people
    SMORES_PER_PERSON = 3
    NUM_PEOPLE = 8

    # Calculate the total number of S'mores needed
    total_smores = SMORES_PER_PERSON * NUM_PEOPLE

    # Calculate the total cost of supplies needed
    SUPPLIES_PER_4_SMORES = 3
    num_batches = total_smores / 4
    total_cost = num_batches * SUPPLIES_PER_4_SMORES

    # Display the total cost of supplies needed
    result = total_cost
    return result

print(solution())