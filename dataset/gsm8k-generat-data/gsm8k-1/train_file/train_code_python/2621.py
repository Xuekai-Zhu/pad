def solution():
    """Napoleon has 17 jelly beans and Sedrich has 4 more jelly beans than Napoleon. If twice the sum of Napoleon and Sedrich's jelly beans is 4 times the number of jelly beans that Mikey has, how many jelly beans does Mikey have?"""
    napoleon_jellybeans = 17
    sedrich_jellybeans = napoleon_jellybeans + 4
    total_jellybeans = napoleon_jellybeans + sedrich_jellybeans
    mikey_jellybeans = total_jellybeans * 2 / 4
    result = mikey_jellybeans
    return result

print(solution())