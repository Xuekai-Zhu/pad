def solution():
    sentence_for_assault = 3  # in months
    sentence_for_poisoning = 24  # in months
    
    # Calculate the total sentence without extension
    total_sentence = sentence_for_assault + sentence_for_poisoning
    
    # Calculate the extension for being a repeat offender
    extension = total_sentence / 3
    
    # Calculate the total sentence with extension
    total_sentence_with_extension = total_sentence + extension
    
    # Convert the sentence to months and return the result
    result = total_sentence_with_extension * 12
    return result

print(solution())