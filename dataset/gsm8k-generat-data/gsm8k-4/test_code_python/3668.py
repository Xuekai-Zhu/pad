def solution():
    """Anderson makes mud masks for spa treatments. In every batch of mud that he mixes, he adds three sprigs of mint, and he adds two green tea leaves for every sprig of mint. He had to switch to a different kind of mud, which makes the other ingredients he adds half as effective. How many green tea leaves should Anderson add to a new batch of mud to get the same efficacy as before?"""
    # Define the number of mint sprigs and green tea leaves in an original batch
    mint_sprigs = 3
    green_tea_leaves = mint_sprigs * 2

    # Calculate the number of green tea leaves required in a new batch with half efficacy
    green_tea_leaves_new = green_tea_leaves * 2

    # Return the result
    result = green_tea_leaves_new
    return result

print(solution())