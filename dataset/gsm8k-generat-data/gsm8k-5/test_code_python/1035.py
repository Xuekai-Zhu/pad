def solution():
    boys = 600  # There are 600 boys at the event
    girls = boys + 400  # The difference between boys and girls is 400, so there are 600 + 400 = 1000 girls
    total = boys + girls  # Calculate the total number of boys and girls
    sixty_percent = 0.6 * total  # Calculate 60% of the total

    result = sixty_percent
    return result

print(solution())