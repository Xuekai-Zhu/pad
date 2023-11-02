def solution():
    friends_in_classes = 6
    friends_in_clubs = friends_in_classes / 2
    keychains_per_friend = 1
    inches_per_keychain = 12

    # Calculate the total number of friends that will receive a keychain
    total_friends = friends_in_classes + friends_in_clubs

    # Calculate the total number of keychains that Shelly will make
    total_keychains = total_friends * keychains_per_friend

    # Calculate the total number of inches of thread that Shelly will need
    total_inches = total_keychains * inches_per_keychain
    result = total_inches
    return result

print(solution())