def solution():
    """Shelly makes braided keychains for her friends at school. Each keychain takes 12 inches of thread to braid. This year, she made six friends in classes and half that number from after-school clubs. She wants to make each of them a keychain. How many inches of thread does Shelly need?"""
    # Define the number of friends
    class_friends = 6
    club_friends = class_friends / 2
    total_friends = class_friends + club_friends

    # Calculate the total length of thread needed
    thread_length = total_friends * 12

    # return the result
    result = thread_length
    return result

print(solution())