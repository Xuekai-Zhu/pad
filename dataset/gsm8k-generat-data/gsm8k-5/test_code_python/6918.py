def solution():
    grocery_texts = 5  # Jennifer's boyfriend sent 5 texts about grocery shopping
    response_texts = 5 * grocery_texts  # Jennifer's boyfriend sent 5 times more texts asking why she wasn't responding
    police_texts = round(0.1 * (grocery_texts + response_texts))  # Jennifer's boyfriend sent 10% of all the previous texts saying he was calling the police

    # Calculate the total number of texts Jennifer's boyfriend sent
    total_texts = grocery_texts + response_texts + police_texts
    result = total_texts
    return result

print(solution())