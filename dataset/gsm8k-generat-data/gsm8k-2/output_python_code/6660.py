def solution():
    """Helga went shopping for a new pair of shoes. At the first store, she tried on 7 pairs of shoes. At the second store, she tried on 2 more pairs than at the first store. At the third store, she did not try on any shoes, but she did buy a scarf. But at the fourth store, she tried on twice as many pairs of shoes as she did at all three other stores combined, before finally choosing a pair to buy. What is the total number of pairs of shoes Helga tried on before buying her new shoes?"""
    first_store = 7
    second_store = first_store + 2
    third_store = 0
    fourth_store = 2 * (first_store + second_store + third_store)
    total_tries = first_store + second_store + third_store + fourth_store
    result = total_tries
    return result

print(solution())