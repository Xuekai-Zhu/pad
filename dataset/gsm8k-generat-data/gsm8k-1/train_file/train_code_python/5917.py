def solution():
    """Jo-Bob hopped into the hot air balloon, released the anchor rope, and pulled on the lift chain, which ignited the flame and provided the warm air that caused the balloon to rise. When the lift chain was pulled, the balloon would rise at a rate of 50 feet per minute. But when the chain was not being pulled, the balloon would slowly descend at a rate of 10 feet per minute. During his balloon ride, he pulled the chain for 15 minutes, then released the rope for 10 minutes, then pulled the chain for another 15 minutes, and finally released the chain and allowed the balloon to slowly descend back to the earth. During his balloon ride, what was the highest elevation reached by the balloon?"""
    chain_pull_time_1 = 15
    chain_release_time = 10
    chain_pull_time_2 = 15
    chain_pull_elevation = 50 * chain_pull_time_1 + 50 * chain_pull_time_2
    release_descent_elevation = 10 * chain_release_time
    highest_elevation = chain_pull_elevation - release_descent_elevation
    result = highest_elevation
    return result

print(solution())