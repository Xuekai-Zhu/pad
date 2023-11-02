def solution():
    """Shelly makes braided keychains for her friends at school. Each keychain takes 12 inches of thread to braid. This year, she made six friends in classes and half that number from after-school clubs. She wants to make each of them a keychain. How many inches of thread does Shelly need?"""
    # Calculate the total number of friends
    total_friends = 6 + (6 / 2)

    # Calculate the total inches of thread needed
    total_thread = total_friends * 12

    # Display the total inches of thread needed
    result = total_thread
    return result

print(solution())