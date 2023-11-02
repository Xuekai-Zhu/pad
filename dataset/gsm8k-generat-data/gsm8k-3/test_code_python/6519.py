def solution():
    """A snail kite is a kind of bird that eats apple snails. On the first day, a snail kite ate 3 snails. Then it eats 2 more snails than it did the day before. How many apple snails in all did a snail kite eat for 5 days?"""
    # Define the number of snails eaten on the first day
    snails_eaten = 3

    # Define the increase in snails eaten per day
    snails_increase = 2

    # Calculate the total number of snails eaten over 5 days
    total_snails = snails_eaten + (snails_eaten + snails_increase) + (snails_eaten + 2*snails_increase) + (snails_eaten + 3*snails_increase) + (snails_eaten + 4*snails_increase)

    # Display the total number of snails eaten
    result = total_snails
    return result

print(solution())