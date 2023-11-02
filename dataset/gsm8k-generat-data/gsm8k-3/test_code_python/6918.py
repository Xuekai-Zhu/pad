def solution():
    """Jennifer's boyfriend left 5 texts about the grocery shopping, 5 times more texts asking why she wasn't responding, and a number of texts equal to 10% of all the texts he sent previously saying he was calling the police. How many texts did he send total?"""
    # Define the number of texts about grocery shopping
    grocery_texts = 5

    # Define the multiplier for the number of texts asking why Jennifer wasn't responding
    response_multiplier = 5

    # Calculate the total number of response texts
    response_texts = grocery_texts * response_multiplier

    # Calculate the number of texts saying he was calling the police
    police_texts = int((grocery_texts + response_texts) * 0.1)

    # Calculate the total number of texts sent
    total_texts = grocery_texts + response_texts + police_texts

    # Display the total number of texts sent
    result = total_texts
    return result

print(solution())