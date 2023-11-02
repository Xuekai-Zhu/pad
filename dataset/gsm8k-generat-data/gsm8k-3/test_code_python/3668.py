def solution():
    """Anderson makes mud masks for spa treatments. In every batch of mud that he mixes, he adds three sprigs of mint, and he adds two green tea leaves for every sprig of mint. He had to switch to a different kind of mud, which makes the other ingredients he adds half as effective. How many green tea leaves should Anderson add to a new batch of mud to get the same efficacy as before?"""
    # Define the original number of sprigs of mint and leaves of green tea
    original_mint = 3
    original_green_tea = 2 * original_mint

    # Calculate the new number of leaves of green tea needed
    new_green_tea = original_green_tea * 2

    # Display the new number of green tea leaves needed
    result = new_green_tea
    return result

print(solution())