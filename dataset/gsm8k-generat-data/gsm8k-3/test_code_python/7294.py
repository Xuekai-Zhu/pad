def solution():
    """Micah bought envelopes to send, and depending on the weight of the envelope he will need more stamps. If an envelope weighs more than 5 pounds, he will need 5 stamps. If it weighs less than that, it will only need 2 stamps. If he bought 52 stamps with 6 envelopes that weigh less than 5 pounds, how many envelopes in total did Micah need to buy?"""
    # Define the number of stamps needed for envelopes weighing less than 5 pounds and more than 5 pounds
    LESS_THAN_5 = 2
    MORE_THAN_5 = 5

    # Define the number of envelopes weighing less than 5 pounds and the total number of stamps used for them
    less_than_5_envelopes = 6
    less_than_5_stamps = less_than_5_envelopes * LESS_THAN_5

    # Calculate the number of stamps used for envelopes weighing more than 5 pounds
    more_than_5_stamps = 52 - less_than_5_stamps

    # Calculate the number of envelopes weighing more than 5 pounds
    more_than_5_envelopes = more_than_5_stamps // MORE_THAN_5

    # Calculate the total number of envelopes needed
    total_envelopes = less_than_5_envelopes + more_than_5_envelopes

    # Display the total number of envelopes needed
    result = total_envelopes
    return result

print(solution())