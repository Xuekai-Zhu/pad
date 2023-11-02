def solution():
    """Harry's birthday was three weeks after the closing of the school. His three friends decided to contribute an equal amount of money to throw him a party. Harry added $30 to the contribution, making the total contribution three times as much as Harry contributed. Calculate the total amount of money that each of Harry's friends contributed."""
    # Define the number of friends
    num_friends = 3

    # Define the amount Harry contributed
    harry_contributed = 30

    # Define the total contribution
    total_contribution = harry_contributed * 4

    # Calculate the amount each friend contributed
    each_friend_contributed = total_contribution / num_friends

    # Display the amount each friend contributed
    result = each_friend_contributed
    return result

print(solution())