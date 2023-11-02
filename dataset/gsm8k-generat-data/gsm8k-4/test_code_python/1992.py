def solution():
    """If 1 ounce of Dawn liquid soap can make 200,000 bubbles, and Dr. Bronner's liquid soap can make twice as many bubbles per ounce as Dawn liquid soap, then how many bubbles can be made from one half ounce of an equal mixture of Dawn and Dr. Bronner's liquid soaps?"""
    # Define the number of bubbles 1 ounce of Dawn soap can make
    dawn_bubbles_per_ounce = 200000

    # Define the number of bubbles 1 ounce of Dr. Bronner's soap can make
    bronner_bubbles_per_ounce = 2 * dawn_bubbles_per_ounce

    # Define the total number of bubbles that can be made from 1 ounce of the mixture
    total_bubbles_per_ounce = dawn_bubbles_per_ounce + bronner_bubbles_per_ounce

    # Define the total number of bubbles that can be made from 1/2 ounce of the mixture
    total_bubbles_per_half_ounce = total_bubbles_per_ounce / 2

    result = total_bubbles_per_half_ounce
    return result

print(solution())