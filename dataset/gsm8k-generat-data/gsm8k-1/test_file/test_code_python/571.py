def solution():
    """At the end of the school year, Kate asked her teacher if she could have the 3 boxes of 64 crayons since they were all worn down to small pieces. The teacher agreed. Kate took the crayons home and decided to make crayon muffins by melting 8 small pieces of crayons together in a muffin tin that she placed in an oven for a few minutes. If she can sell her muffin crayons for $1.50 each, how much money can Kate make?"""
    boxes_of_crayons = 3
    crayons_per_box = 64
    total_crayons = boxes_of_crayons * crayons_per_box
    crayons_per_muffin = 8
    muffins = total_crayons // crayons_per_muffin
    price_per_muffin = 1.5
    money_made = muffins * price_per_muffin
    result = money_made
    return result

print(solution())