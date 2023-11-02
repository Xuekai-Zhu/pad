def solution():
    
    # Define the total number of unicorns
    total_unicorns = 27

    # Calculate the number of unicorns in the Highlands
    highlands_unicorns = total_unicorns // 3

    # Calculate the number of female Scottish unicorns
    female_unicorns = total_unicorns - highlands_unicorns

    # Display the number of female Scottish unicorns
    result = female_unicorns
    return result

print(solution())