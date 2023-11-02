def solution():
    """Harper collected 30% more pieces of Halloween candy than her sister Maggie, who only collected 50 pieces.
    Neil collected 40% more candy than Harper. How much candy did Neil get on Halloween?"""
    # Calculate how much candy Harper collected
    maggie_candy = 50
    harper_candy = maggie_candy * 1.3

    # Calculate how much candy Neil collected
    neil_candy = harper_candy * 1.4

    # Display the total amount of candy Neil collected
    result = neil_candy
    return result

print(solution())