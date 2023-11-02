def solution():
    """Helga went shopping for a new pair of shoes. At the first store, she tried on 7 pairs of shoes. At the second store, she tried on 2 more pairs than at the first store. At the third store, she did not try on any shoes, but she did buy a scarf.  But at the fourth store, she tried on twice as many pairs of shoes as she did at all three other stores combined, before finally choosing a pair to buy.  What is the total number of pairs of shoes Helga tried on before buying her new shoes?"""
    # Number of pairs of shoes Helga tried on at the first store
    store1_shoes = 7

    # Number of pairs of shoes Helga tried on at the second store
    store2_shoes = store1_shoes + 2

    # Number of pairs of shoes Helga tried on at the third store
    store3_shoes = 0

    # Number of pairs of shoes Helga tried on at the fourth store
    store4_shoes = 2 * (store1_shoes + store2_shoes + store3_shoes)

    # Total number of pairs of shoes Helga tried on before buying
    total_shoes = store1_shoes + store2_shoes + store3_shoes + store4_shoes

    # Display the total number of pairs of shoes Helga tried on
    result = total_shoes
    return result

print(solution())