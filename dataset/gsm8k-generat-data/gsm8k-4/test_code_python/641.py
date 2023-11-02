def solution():
    """Alex makes luxury dresses out of silk. Each dress needs 5 meters of silk and Alex has 600 meters of silk in storage. His friends also want to learn how to make these dresses so Alex gives all 5 of them 20 meters of silk each. He uses the rest to make dresses himself. How many dresses can Alex make?"""
    # Define the amount of silk needed for each dress and the amount of silk in storage
    SILK_PER_DRESS = 5
    silk_in_storage = 600

    # Calculate the amount of silk given to friends and the amount remaining for Alex
    silk_given = 5 * 20
    silk_remaining = silk_in_storage - silk_given

    # Calculate the number of dresses Alex can make with the remaining silk
    dresses = silk_remaining // SILK_PER_DRESS

    result = dresses
    return result

print(solution())