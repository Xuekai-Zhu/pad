def solution():
    """Harry's birthday was three weeks after the closing of the school. His three friends decided to contribute an equal amount of money to throw him a party. Harry added $30 to the contribution, making the total contribution three times as much as Harry contributed. Calculate the total amount of money that each of Harry's friends contributed."""
    total_contribution = 3 * (x + 30)
    x = total_contribution / 4
    each_friend_contributed = x / 3
    result = each_friend_contributed
    return result

print(solution())