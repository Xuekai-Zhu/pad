def solution():
    """Hanna has twice as many erasers as Rachel. Rachel has three less than one-half as many erasers as Tanya has red erasers. If Tanya has 20 erasers, and half of them are red, how many erasers does Hanna have?"""
    # Define the total number of red erasers
    total_red_erasers = 20 / 2

    # Calculate Tanya's erasers
    tanya_erasers = total_red_erasers * 2

    # Calculate Rachel's erasers
    rachel_erasers = (tanya_erasers / 2) - 3

    # Calculate Hanna's erasers
    hanna_erasers = rachel_erasers * 2

    result = hanna_erasers
    return result

print(solution())