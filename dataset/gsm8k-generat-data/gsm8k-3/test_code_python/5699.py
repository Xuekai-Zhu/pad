def solution():
    """Yanna bought 60 apples. She gave eighteen apples to Zenny. She gave six more apples to Andrea and kept the rest. How many apples did she keep?"""
    # Define the total number of apples Yanna bought
    total_apples = 60

    # Define the number of apples Yanna gave to Zenny
    zenny_apples = 18

    # Define the number of apples Yanna gave to Andrea
    andrea_apples = 6

    # Calculate the number of apples Yanna kept
    kept_apples = total_apples - zenny_apples - andrea_apples

    # Display the number of apples Yanna kept
    result = kept_apples
    return result

print(solution())