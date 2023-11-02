def solution():
    """Paul is collecting license plates from different states. He has plates from 40 different states. For each percentage point of total US states that he has, his parents will give him $2. How much does he earn from them?"""
    # Define the total number of US states
    total_states = 50

    # Calculate the percentage of states that Paul has plates from
    percentage = (40 / total_states) * 100

    # Calculate the amount of money Paul earns
    earnings = percentage * 2

    # return the result
    result = earnings
    return result

print(solution())