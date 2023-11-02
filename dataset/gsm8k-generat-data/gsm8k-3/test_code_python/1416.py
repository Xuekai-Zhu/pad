def solution():
    """The company's data entry team had 5 employees working on a large project.  Rudy types 64 words per minute, Joyce types 76 words per minute, Gladys types 91 words per minute, Lisa types 80 words per minute and Mike types 89 words per minute.  What is the team's average typed words per minute?"""
    # Define the typing speeds of each employee
    rudy_speed = 64
    joyce_speed = 76
    gladys_speed = 91
    lisa_speed = 80
    mike_speed = 89

    # Calculate the total typing speed of the team
    total_speed = rudy_speed + joyce_speed + gladys_speed + lisa_speed + mike_speed

    # Calculate the average typing speed
    avg_speed = total_speed / 5

    # Display the average typing speed
    result = avg_speed
    return result

print(solution())