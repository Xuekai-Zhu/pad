def solution():
    """The chances of making the junior high basketball team start at 10% if you're 66 inches and increase 10% for every additional inch of height. Devin starts out as 65 inches tall, then grows 3 inches. What are his chances of making the basketball team?"""
    # Initialize the starting height and chances of making the team
    starting_height = 65
    starting_chances = 0.1

    # Calculate the new height and chances after growing 3 inches
    new_height = starting_height + 3
    new_chances = starting_chances + ((new_height - 66) * 0.1)

    # Round the chances to two decimal places
    rounded_chances = round(new_chances, 2)

    # return the result
    result = rounded_chances
    return result

print(solution())