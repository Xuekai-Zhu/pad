def solution():
    quarters_per_jar = 160  # Each jar can hold 160 quarters
    total_quarters = quarters_per_jar * 5  # Jenn has 5 jars full of quarters
    total_dollars = total_quarters * 0.25  # Each quarter is worth $0.25

    # Calculate how much money Jenn will have left after buying the bike
    remaining_dollars = total_dollars - 180
    result = remaining_dollars
    return result

print(solution())