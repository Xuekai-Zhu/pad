def solution():
    
    class_friends = 6
    club_friends = class_friends / 2
    total_friends = class_friends + club_friends
    thread_per_keychain = 12
    total_thread = total_friends * thread_per_keychain
    result = total_thread
    return result

print(solution())