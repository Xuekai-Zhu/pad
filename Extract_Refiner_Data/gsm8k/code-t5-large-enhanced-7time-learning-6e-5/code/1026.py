def solution():
    
    # Define the probability of Marcus having a substitute teacher who won't collect the homework
    NEG_PROBABILITY = 50

    # Define the probability of Marcus giving everyone an extension
    EXTENSION_PROBABILITY = 40

    # Define the probability of Marcus having a personal extension
    PERSON_PROBABILITY = 20

    # Calculate the probability of Marcus having a homework tomorrow
    tomorrow_prob = NEG_PROBABILITY * (1 - EXTENSION_PROBABILITY)

    # Calculate the probability of Marcus having a homework tomorrow after the accident
    tomorrow_prob *= 1 - EXTENSION_PROBABILITY

    # Convert the probability to a percentage
    percentage = tomorrow_prob * 100

    # Display the percentage chance
    result = percentage
    return result

print(solution())