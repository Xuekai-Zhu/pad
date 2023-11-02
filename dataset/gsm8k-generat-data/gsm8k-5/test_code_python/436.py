def solution():
    num_pencils = 60  # Catherine had an equal number of pencils and pens, so she also had 60 pencils
    num_friends = 7  # Catherine gave pens and pencils to 7 friends
    pens_per_friend = 8  # Catherine gave 8 pens to each friend
    pencils_per_friend = 6  # Catherine gave 6 pencils to each friend

    # Calculate the total number of pens and pencils Catherine gave to her friends
    total_pens_given = num_friends * pens_per_friend
    total_pencils_given = num_friends * pencils_per_friend

    # Calculate the number of pens and pencils Catherine kept for herself
    num_pens_left = num_pencils - total_pens_given + 8  # Catherine gave 8 extra pens to her friends
    num_pencils_left = num_pencils - total_pencils_given + 6  # Catherine gave 6 extra pencils to her friends

    # Return the number of pens and pencils Catherine had left
    result = (num_pens_left, num_pencils_left)
    return result

print(solution())