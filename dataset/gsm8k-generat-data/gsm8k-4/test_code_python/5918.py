def solution():
    """Jo-Bob hopped into the hot air balloon, released the anchor rope, and pulled on the lift chain, which ignited the flame and provided the warm air that caused the balloon to rise. When the lift chain was pulled, the balloon would rise at a rate of 50 feet per minute. But when the chain was not being pulled, the balloon would slowly descend at a rate of 10 feet per minute. During his balloon ride, he pulled the chain for 15 minutes, then released the rope for 10 minutes, then pulled the chain for another 15 minutes, and finally released the chain and allowed the balloon to slowly descend back to the earth. During his balloon ride, what was the highest elevation reached by the balloon?"""
    # Define the initial height of the balloon
    height = 0

    # Calculate the height gain during the first 15 minutes
    height += 50 * 15

    # Calculate the height loss during the next 10 minutes
    height -= 10 * 10

    # Calculate the height gain during the next 15 minutes
    height += 50 * 15

    # Calculate the height loss during the descent
    height -= 10 * 20

    # Return the highest elevation reached by the balloon
    result = height
    return result

print(solution())