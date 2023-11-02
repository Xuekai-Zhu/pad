def solution():
    friends_in_school = 6  # Shelly made 6 friends in classes
    friends_in_clubs = friends_in_school / 2  # Shelly made half that number in after-school clubs
    total_friends = friends_in_school + friends_in_clubs  # Shelly wants to make each friend a keychain

    # Calculate the total inches of thread Shelly needs
    total_inches_of_thread = total_friends * 12

    result = total_inches_of_thread
    return result

print(solution())