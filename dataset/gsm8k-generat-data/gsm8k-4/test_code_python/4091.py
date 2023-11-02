def solution():
    """Ryan works in an office that has an even number of men and women working there.  Ryan participates in a meeting composed of 4 men and 6 women who are pulled from the office floor.   This reduces the number of women working on the office floor by 20%.  How many people work at Ryan's office?"""
    # Define the number of women pulled from the office floor
    women_pulled = 6

    # Calculate the percentage decrease in the number of women working on the office floor
    percentage_decrease = 20

    # Calculate the total percentage of women originally working on the office floor
    # (since there are an even number of men and women, this is also the percentage of men)
    total_percentage = 100 / (1 - percentage_decrease / 100)

    # Calculate the total number of people working in the office
    total_people = (women_pulled / (total_percentage / 100)) * 100

    result = total_people
    return result

print(solution())