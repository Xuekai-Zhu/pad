def solution():
    """Twenty gallons of tea were poured into 80 containers. Geraldo drank 3.5 containers. How many pints of tea did Geraldo drink?"""
    gallons = 20
    containers = 80
    tea_per_container = gallons * 128 / containers
    geraldo_containers = 3.5
    geraldo_pints = geraldo_containers * tea_per_container / 2
    result = geraldo_pints
    return result

print(solution())