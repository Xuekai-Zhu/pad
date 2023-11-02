def solution():
    initial_maggots = 10
    eaten_maggots = 1 + 3  # the beetle ate 1 maggot initially and 3 more later
    remaining_maggots = initial_maggots - eaten_maggots
    total_maggots = 20
    
    # Calculate the number of maggots fed to the beetle the second time
    num_second_feed = total_maggots - remaining_maggots
    
    result = num_second_feed
    return result

print(solution())