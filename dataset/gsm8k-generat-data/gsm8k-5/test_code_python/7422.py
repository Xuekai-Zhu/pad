def solution():
    initial_fill = 0  # Mark initially fills the bowl with some amount of punch
    remaining_punch = 0  # Amount of punch remaining after his cousin and friend drink some of it
    refill = 4  # Mark refills the bowl with 4 more gallons of punch
    sally_drinks = 2  # Sally drinks 2 gallons of punch
    final_fill = 12  # Mark adds 12 gallons of punch to completely fill the bowl

    # Calculate the amount of punch remaining after Mark's cousin drinks half the bowl
    remaining_punch = initial_fill / 2

    # Calculate the amount of punch remaining after Sally drinks 2 gallons
    remaining_punch = remaining_punch - sally_drinks

    # Calculate the amount of punch Mark initially added
    initial_fill = remaining_punch - refill - final_fill
    result = initial_fill
    return result

print(solution())