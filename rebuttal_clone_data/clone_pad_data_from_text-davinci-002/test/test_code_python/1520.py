def solution():
    thread_per_keychain = 12
    num_friends_in_classes = 6
    num_friends_in_clubs = num_friends_in_classes / 2
    total_friends = num_friends_in_classes + num_friends_in_clubs
    total_thread = total_friends * thread_per_keychain
    result = total_thread
    return result

print(solution())