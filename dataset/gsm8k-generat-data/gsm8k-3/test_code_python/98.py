def solution():
    """Hector purchased a container of gumballs. He gave 4 to Todd, then he gave twice as many as he had given Todd to Alisha, and then he gave 5 less than four times as many to Bobby as he had given to Alisha. If Hector had 6 gumballs remaining, what is the total number of gumballs that Hector purchased?"""
    # Define the number of gumballs Hector started with
    hector_start = None

    # Define the number of gumballs Hector gave to Todd
    hector_todd = 4

    # Define the number of gumballs Hector gave to Alisha
    hector_alisha = hector_todd * 2

    # Define the number of gumballs Hector gave to Bobby
    hector_bobby = 4 * hector_alisha - 5

    # Calculate the number of gumballs Hector had remaining
    hector_remaining = hector_start - hector_todd - hector_alisha - hector_bobby

    # Calculate the total number of gumballs Hector purchased
    hector_total = hector_start + hector_remaining

    result = hector_total
    return result

print(solution())