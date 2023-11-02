def solution():
    spool_length = 20  # Each spool is 20 feet long
    num_spools = 3  # John buys 3 spools
    necklace_length = 4  # 4 feet of wire is needed to make one necklace

    # Calculate the total length of wire John has
    total_length = spool_length * num_spools

    # Calculate the number of necklaces John can make
    num_necklaces = total_length // necklace_length  # Use integer division to get a whole number of necklaces
    result = num_necklaces
    return result

print(solution())