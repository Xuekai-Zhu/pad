def solution():
    """Nancy is crafting clay pots to sell. She creates 12 clay pots on Monday, twice as many on Tuesday, a few more on Wednesday, then ends the week with 50 clay pots. How many did she create on Wednesday?"""
    # Define the number of clay pots Nancy created on Monday and Tuesday
    monday_pots = 12
    tuesday_pots = monday_pots * 2

    # Calculate the total number of pots Nancy created so far
    total_pots = monday_pots + tuesday_pots

    # Calculate the number of pots Nancy created on Wednesday
    wednesday_pots = 50 - total_pots

    # Display the number of pots Nancy created on Wednesday
    result = wednesday_pots
    return result

print(solution())