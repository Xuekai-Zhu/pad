def solution():
    # Define the original sentence lengths in months
    assault_sentence = 3
    poisoning_sentence = 24

    # Calculate the total sentence length before extension
    total_sentence = assault_sentence + poisoning_sentence

    # Calculate the length of the extension
    extension_length = total_sentence / 3

    # Add the extension to the total sentence length
    extended_sentence = total_sentence + extension_length

    # Convert the sentence length to months and round to the nearest integer
    months_in_jail = round(extended_sentence * 12)

    result = months_in_jail
    return result

print(solution())