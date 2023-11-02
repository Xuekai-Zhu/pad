def solution():
    num_ducks = 150
    diff = 10
    num_chickens = (num_ducks - diff) / 4  # Calculate the number of chickens
    total_birds = num_chickens + num_ducks  # Calculate the total number of birds
    result = total_birds
    return result

print(solution())