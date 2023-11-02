def solution():
    """Andy can get 50 demerits in a month before getting fired. If he got 2 demerits per instance for showing up late 6 times and 15 demerits for making an inappropriate joke, how many more demerits can he get this month before getting fired?"""
    # Define the maximum number of demerits allowed in a month
    MAX_DEMERITS = 50

    # Calculate the number of demerits Andy received
    demerits_late = 2 * 6
    demerits_joke = 15
    total_demerits = demerits_late + demerits_joke

    # Calculate the remaining demerits Andy can get before getting fired
    remaining_demerits = MAX_DEMERITS - total_demerits

    # Display the remaining demerits
    result = remaining_demerits
    return result

print(solution())