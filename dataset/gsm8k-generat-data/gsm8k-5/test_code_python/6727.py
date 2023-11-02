def solution():
    martha_rats = 3
    martha_birds = 7
    martha_total = martha_rats + martha_birds  # Calculate the total number of animals Martha's cat caught

    # Calculate the number of animals Cara's cat caught
    cara_total = (5 * martha_total) - 3

    result = cara_total
    return result

print(solution())