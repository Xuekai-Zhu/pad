def solution():
    """James can make 4 hats out of one yard of velvet. He needs three yards of velvet to make a cloak. How much velvet does he need to make 6 cloaks and 12 hats?"""
    # Define the number of hats James can make with one yard of velvet
    hats_per_yard = 4

    # Define the amount of velvet needed to make one cloak
    velvet_per_cloak = 3

    # Calculate the total amount of velvet needed to make 6 cloaks
    total_velvet_cloaks = velvet_per_cloak * 6

    # Calculate the total number of hats needed
    total_hats = 12

    # Calculate the total amount of velvet needed to make 12 hats
    total_velvet_hats = total_hats / hats_per_yard

    # Calculate the total amount of velvet needed for both cloaks and hats
    total_velvet = total_velvet_cloaks + total_velvet_hats

    result = total_velvet
    return result

print(solution())