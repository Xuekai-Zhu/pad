def solution():
    """The basketball team went to the steakhouse to eat dinner. The first player ate a 6-ounce steak. The second player ate beef tips, containing 8 beef tips, each an ounce in size. The third player ate a one-pound steak. And the fourth and fifth players ordered vegetarian meals. In total, how many ounces of meat were consumed by the team?"""
    player1_steak = 6
    player2_beef_tips = 8 * 1
    player3_steak = 16
    total_meat = player1_steak + player2_beef_tips + player3_steak
    result = total_meat
    return result

print(solution())