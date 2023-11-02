def solution():
    """Mark plants some strawberries in his backyard. Every month, the number of strawberry plants doubles. After 3 months, Mark digs up 4 strawberry plants and gives them to his friend.  If he still has 20 strawberry plants, how many did he initially plant?"""
    # Define the initial number of strawberry plants
    num_plants = 0

    # Calculate the number of plants after each month
    for i in range(3):
        num_plants *= 2

    # Subtract the 4 plants that were dug up
    num_plants -= 4

    # Add back the 20 remaining plants
    num_plants += 20

    # Display the initial number of plants
    result = num_plants
    return result

print(solution())