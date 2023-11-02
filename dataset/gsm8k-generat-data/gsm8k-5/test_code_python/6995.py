def solution():
    total_pets = 70  # Bill thought he bought 70 pets
    chihuahuas = total_pets / 7  # Assume all the pets were chihuahuas (1/7th part of pets are chihuahuas)
    rats = 6 * chihuahuas  # Number of rats is 6 times the number of chihuahuas

    # Calculate the actual number of rats
    actual_rats = total_pets - chihuahuas

    result = actual_rats
    return result

print(solution())