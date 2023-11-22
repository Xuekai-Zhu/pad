def solution():
    
    # Define the number of times each friend pressed the doorbell
    fourth_friend_presses = 60
    second_friend_presses = 1.25 * fourth_friend_presses
    third_friend_presses = 10 * fourth_friend_presses

    # Calculate the total number of doorbell rings
    total_rings = 20 + second_friend_presses + third_friend_presses + fourth_friend_presses

    # Display the total number of doorbell rings
    result = total_rings
    return result

print(solution())