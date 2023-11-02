def solution():
    """ It's Yvette's turn to treat herself and her three best friends to a round of ice cream sundaes. Alicia orders the peanut butter sundae for $7.50. Brant orders the Royal banana split sundae for $10.00. Josh orders the death by chocolate sundae for $8.50 and Yvette orders the cherry jubilee sundae for $9.00. She leaves her waiter a 20% tip. How much will her final bill be? """
    peanut_butter_sundae = 7.5
    royal_banana_split = 10
    death_by_chocolate = 8.5
    cherry_jubilee = 9
    subtotal = peanut_butter_sundae + royal_banana_split + death_by_chocolate + cherry_jubilee
    tip = subtotal * 0.2
    total = subtotal + tip
    result = total
    return result

print(solution())