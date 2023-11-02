def solution():
    """James runs a TV show and there are 5 main characters and 4 minor characters. He pays the minor characters $15,000 each episode. He paid the major characters three times as much. How much does he pay per episode?"""
    # Define the number of main and minor characters and the pay rate for minor characters
    num_main = 5
    num_minor = 4
    pay_minor = 15000

    # Calculate the pay rate for each major character
    pay_main = pay_minor * 3

    # Calculate the total pay for all characters
    total_pay = (num_main * pay_main) + (num_minor * pay_minor)

    # Calculate the pay per episode
    pay_per_episode = total_pay / 1

    result = pay_per_episode
    return result

print(solution())