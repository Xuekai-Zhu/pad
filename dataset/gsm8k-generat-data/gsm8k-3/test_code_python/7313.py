def solution():
    """James can make 4 hats out of one yard of velvet. He needs three yards of velvet to make a cloak. How much velvet does he need to make 6 cloaks and 12 hats?"""
    # Calculate the amount of velvet needed for one hat
    velvet_per_hat = 1/4 # one yard of velvet makes 4 hats

    # Calculate the amount of velvet needed for one cloak
    velvet_per_cloak = 3

    # Calculate the total amount of velvet needed for 12 hats
    velvet_for_hats = 12 * velvet_per_hat

    # Calculate the total amount of velvet needed for 6 cloaks
    velvet_for_cloaks = 6 * velvet_per_cloak

    # Calculate the total amount of velvet needed for all the items
    total_velvet_needed = velvet_for_hats + velvet_for_cloaks

    # Display the total amount of velvet needed
    result = total_velvet_needed
    return result

print(solution())