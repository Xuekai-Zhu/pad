def solution():
    maggots_eaten = 1  # The beetle only ate 1 maggot during the first feeding
    maggots_left = 10 - maggots_eaten  # Bogan had to throw out the remaining maggots
    maggots_eaten = 3  # The beetle ate 3 maggots during the second feeding
    total_maggots = 20  # Bogan served a total of 20 maggots

    # Calculate the number of maggots Bogan attempted to feed the beetle the second time
    attempted_maggots = total_maggots - maggots_left - maggots_eaten
    result = attempted_maggots
    return result

print(solution())