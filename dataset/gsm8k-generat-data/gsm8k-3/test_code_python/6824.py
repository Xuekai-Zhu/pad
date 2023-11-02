def solution():
    """Simone ate 1/2 of an apple each day for 16 days. Lauri ate 1/3 of an apple each day for 15 days. How many apples did the two girls eat altogether?"""
    # Calculate the amount of apples Simone ate
    simone_apples = 16 * 0.5

    # Calculate the amount of apples Lauri ate
    lauri_apples = 15 * 1/3

    # Calculate the total amount of apples eaten by both girls
    total_apples = simone_apples + lauri_apples

    # Display the total amount of apples eaten
    result = total_apples
    return result

print(solution())