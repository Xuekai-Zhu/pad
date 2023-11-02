def solution():
    # Define the earnings for broccoli and carrots
    broccoli_earnings = 57
    carrot_earnings = 2 * broccoli_earnings

    # Calculate the earnings for spinach
    spinach_earnings = 16 + 0.5 * carrot_earnings

    # Calculate the total earnings from broccoli, carrots, and spinach
    total_earnings = broccoli_earnings + carrot_earnings + spinach_earnings

    # Calculate the earnings for cauliflower sales
    cauliflower_earnings = 380 - total_earnings
    result = cauliflower_earnings
    return result

print(solution())