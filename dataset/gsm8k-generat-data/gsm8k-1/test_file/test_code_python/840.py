def solution():
    """Peter has twice as many socks as Jack and half times as many dishes as jack. Jack collected twice as many dishes as socks in the store. If jack collected 60 dishes, calculate the total number of socks and dishes they have together?"""
    jack_socks = 30  # since Peter has twice as many socks as Jack, and we know that Jack collected twice as many dishes as socks, we can work backwards to find that Jack has 30 socks
    peter_socks = 60  # since Peter has twice as many socks as Jack, he has 60 socks
    jack_dishes = 60
    peter_dishes = jack_dishes / 2  # since Peter has half the number of dishes as Jack, we can find that he has 30 dishes
    total_socks = jack_socks + peter_socks
    total_dishes = jack_dishes + peter_dishes
    result = total_socks + total_dishes
    return result

print(solution())