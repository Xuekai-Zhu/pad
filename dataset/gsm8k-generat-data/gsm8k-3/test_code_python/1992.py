def solution():
    """If 1 ounce of Dawn liquid soap can make 200,000 bubbles, and Dr. Bronner's liquid soap can make twice as many bubbles per ounce as Dawn liquid soap, then how many bubbles can be made from one half ounce of an equal mixture of Dawn and Dr. Bronner's liquid soaps?"""
    # Define the number of bubbles each soap can make per ounce
    DAWN_BUBBLES_PER_OUNCE = 200000
    DR_BRONNERS_BUBBLES_PER_OUNCE = DAWN_BUBBLES_PER_OUNCE * 2

    # Define the volume of the soap mixture
    soap_mixture_volume = 0.5 # half ounce

    # Calculate the volume of each soap in the mixture
    dawn_volume = soap_mixture_volume / 2
    dr_bronners_volume = soap_mixture_volume / 2

    # Calculate the number of bubbles from each soap
    dawn_bubbles = dawn_volume * DAWN_BUBBLES_PER_OUNCE
    dr_bronners_bubbles = dr_bronners_volume * DR_BRONNERS_BUBBLES_PER_OUNCE

    # Calculate the total number of bubbles
    total_bubbles = dawn_bubbles + dr_bronners_bubbles

    # Display the total number of bubbles
    result = total_bubbles
    return result

print(solution())