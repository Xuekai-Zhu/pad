def solution():
    """Enid and Aaron are knitting clothes for their store. Aaron makes 10 scarves and 5 sweaters, and Enid makes 8 sweaters. If a scarf uses 3 balls of wool and a sweater uses 4 balls of wool, how many balls of wool did Enid and Aaron use in total?"""
    # Define the number of scarves and sweaters made by Aaron
    aaron_scarves = 10
    aaron_sweaters = 5

    # Define the number of sweaters made by Enid
    enid_sweaters = 8

    # Define the number of balls of wool used for each scarf and sweater
    SCARF_WOOL = 3
    SWEATER_WOOL = 4

    # Calculate the total number of balls of wool used by Aaron
    aaron_wool = (aaron_scarves * SCARF_WOOL) + (aaron_sweaters * SWEATER_WOOL)

    # Calculate the total number of balls of wool used by Enid
    enid_wool = enid_sweaters * SWEATER_WOOL

    # Calculate the total number of balls of wool used by both Aaron and Enid
    total_wool = aaron_wool + enid_wool

    # Display the total number of balls of wool used
    result = total_wool
    return result

print(solution())