def solution():
    # Calculate the number of boys on the team
    boys = 0.6 * 50

    # Calculate the number of girls on the team
    girls = 50 - boys

    # Calculate the number of junior girls
    junior_girls = 0.5 * 0.4 * girls

    result = junior_girls
    return result

print(solution())