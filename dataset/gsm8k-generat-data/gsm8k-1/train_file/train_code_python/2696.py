def solution():
    """Shelly makes braided keychains for her friends at school. Each keychain takes 12 inches of thread to braid. This year, she made six friends in classes and half that number from after-school clubs. She wants to make each of them a keychain. How many inches of thread does Shelly need?"""
    friends_in_classes = 6
    friends_in_clubs = friends_in_classes / 2
    total_friends = friends_in_classes + friends_in_clubs
    inches_per_keychain = 12
    thread_needed = total_friends * inches_per_keychain
    result = thread_needed
    return result

print(solution())