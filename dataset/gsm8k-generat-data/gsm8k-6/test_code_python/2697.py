def solution():
    # Calculate the total number of friends Shelly needs to make keychains for
    total_friends = 6 + (6/2)  # She made 6 friends in classes and half that number from after-school clubs

    # Calculate the total inches of thread required for all the keychains
    total_thread = total_friends * 12  # Each keychain takes 12 inches of thread to braid

    result = total_thread
    return result

print(solution())