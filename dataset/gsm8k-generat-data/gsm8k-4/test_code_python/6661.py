def solution():
    """Helga went shopping for a new pair of shoes. At the first store, she tried on 7 pairs of shoes. At the second store, she tried on 2 more pairs than at the first store. At the third store, she did not try on any shoes, but she did buy a scarf. But at the fourth store, she tried on twice as many pairs of shoes as she did at all three other stores combined, before finally choosing a pair to buy. What is the total number of pairs of shoes Helga tried on before buying her new shoes?"""
    
    # Initialize the number of shoes tried on
    shoes_tried_on = 0
    
    # At the first store she tried 7 shoes
    shoes_tried_on += 7
    
    # At the second store, she tried on 2 more pairs than at the first store
    shoes_tried_on += (7 + 2)
    
    # At the third store, she did not try on any shoes, but she bought a scarf
    # No shoes were tried on at this store
    # Add 0 to the shoes_tried_on variable
    
    # At the fourth store, she tried on twice as many pairs of shoes as at all three other stores combined
    shoes_tried_on += (7 + 9 + 0) * 2
    
    # Total number of pairs of shoes tried on before buying new shoes
    total_shoes_tried_on = shoes_tried_on
    
    result = total_shoes_tried_on
    return result

print(solution())