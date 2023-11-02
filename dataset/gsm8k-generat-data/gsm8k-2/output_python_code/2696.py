def solution():
    """Shelly makes braided keychains for her friends at school. Each keychain takes 12 inches of thread to braid. This year, she made six friends in classes and half that number from after-school clubs. She wants to make each of them a keychain. How many inches of thread does Shelly need?"""
    class_friends = 6
    club_friends = class_friends / 2
    total_friends = class_friends + club_friends
    thread_per_keychain = 12
    total_thread = total_friends * thread_per_keychain
    result = total_thread
    return result

print(solution())