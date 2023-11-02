def solution():
    # Calculate the total amount of maize stored over 2 years (24 months)
    total_maize = 24  # one tonne per month
    # Subtract 5 tonnes stolen and add 8 tonnes donated
    final_maize = total_maize - 5 + 8
    result = final_maize
    return result

print(solution())