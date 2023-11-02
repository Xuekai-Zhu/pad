def solution():
    """The ratio of boys to girls at the dance was 3:4. There were 60 girls at the dance. The teachers were 20% of the number of boys. How many people were at the dance?"""
    # Define the ratio of boys to girls
    BOYS_TO_GIRLS = 3/4

    # Calculate the number of girls
    girls = 60

    # Calculate the number of boys
    boys = BOYS_TO_GIRLS * girls

    # Calculate the number of teachers
    teachers = 0.2 * boys

    # Calculate the total number of people at the dance
    total_people = girls + boys + teachers

    # Display the total number of people
    result = total_people
    return result

print(solution())