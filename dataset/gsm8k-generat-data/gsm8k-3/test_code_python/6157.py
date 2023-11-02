def solution():
    """A performing magician has a disappearing act where he makes a random member of his audience disappear and reappear. Unfortunately, one-tenth of the time, the audience member never reappears. However, one-fifth of the time, two people reappear instead of only one. If the magician has put on 100 performances of the act this year, how many people have reappeared?"""
    
    # Define the probability of an audience member not reappearing
    prob_no_return = 0.1

    # Define the probability of two people reappearing
    prob_two_return = 0.05

    # Define the number of performances
    num_performances = 100

    # Calculate the total number of people who disappeared
    num_disappeared = num_performances

    # Calculate the number of people who never reappeared
    num_no_return = int(num_disappeared*prob_no_return)

    # Calculate the number of people who reappeared solo
    num_solo_return = num_performances - num_no_return

    # Calculate the number of people who reappeared in pairs
    num_two_return = int(num_solo_return*prob_two_return)

    # Calculate the total number of people who reappeared
    total_return = num_solo_return + num_two_return*2

    # Display the total number of people who reappeared
    result = total_return
    return result

print(solution())