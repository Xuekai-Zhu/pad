def solution():
    """Jennifer's boyfriend left 5 texts about the grocery shopping, 5 times more texts asking why she wasn't responding, and a number of texts equal to 10% of all the texts he sent previously saying he was calling the police. How many texts did he send total?"""
    # Define the number of texts about grocery shopping
    grocery_texts = 5

    # Define the number of times he asked why she wasn't responding
    response_texts = grocery_texts * 5

    # Define the number of texts he sent about calling the police
    police_texts = int((grocery_texts + response_texts) * 0.1)

    # Calculate the total number of texts
    total_texts = grocery_texts + response_texts + police_texts

    # Display the result
    result = total_texts
    return result

print(solution())