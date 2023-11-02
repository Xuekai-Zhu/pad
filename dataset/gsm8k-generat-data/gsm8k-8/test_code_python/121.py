def solution():
    # Calculate the total blocks filled by Stella and Twinkle for 4 hours of work
    total_blocks_filled = 2 * 250 * 4

    # Calculate the remaining blocks needed to fill the truck
    remaining_blocks = 6000 - total_blocks_filled

    # Calculate the total number of people working on filling the truck
    total_people = 2 + 6

    # Calculate the number of hours it will take for all the people to fill the remaining blocks
    hours_needed = remaining_blocks / (total_people * 250)

    # Calculate the total number of hours to fill the truck
    total_hours = 4 + hours_needed
    
    result = total_hours
    return result

print(solution())