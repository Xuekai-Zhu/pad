def solution():
    """James runs a TV show and there are 5 main characters and 4 minor characters.  He pays the minor characters $15,000 each episode.  He paid the major characters three times as much.  How much does he pay per episode?"""
    # Define the pay for the minor characters
    MINOR_PAY = 15000

    # Define the number of major and minor characters
    num_major = 5
    num_minor = 4

    # Calculate the pay for the major characters
    major_pay = num_major * MINOR_PAY * 3

    # Calculate the total pay per episode
    total_pay = major_pay + (num_minor * MINOR_PAY)

    # Display the total pay per episode
    result = total_pay
    return result

print(solution())