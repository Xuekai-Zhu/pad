def solution():
    final_length = 140  # The final design is 140cm long
    original_length = final_length / 0.5  # Shania's original length is 50% of its original length
    lace_trim = 20  # Shania adds 20cm to the bottom of the dress with a lace trim

    # Calculate the original length of the dress
    original_length = original_length + lace_trim
    result = original_length
    return result

print(solution())