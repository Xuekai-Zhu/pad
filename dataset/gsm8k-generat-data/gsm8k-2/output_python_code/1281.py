def solution():
    """Karen had the giant box of crayons, containing twice as many crayons as were in Beatrice's box. But Beatrice's box contained twice as many crayons as were in Gilbert's box of crayons. And Gilbert had four times as many crayons as were in Judah's box of crayons. If Karen's box contained 128 crayons, how many crayons were in Judah's box?"""
    karen_crayons = 128
    beatrice_crayons = karen_crayons // 2
    gilbert_crayons = beatrice_crayons // 2
    judah_crayons = gilbert_crayons // 4
    result = judah_crayons
    return result

print(solution())