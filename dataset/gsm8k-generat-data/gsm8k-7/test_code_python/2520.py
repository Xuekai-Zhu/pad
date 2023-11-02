def solution():
    grenada_supplies = 6000
    grenada_guns = grenada_supplies // 2
    grenada_tractors = (grenada_supplies * 3) // 4
    grenada_uniforms = grenada_supplies * 30

    rockefeller_guns = grenada_guns * 2 + 3000
    rockefeller_tractors = grenada_tractors * 3 - 400
    rockefeller_uniforms = grenada_uniforms * 30

    total_supplies = rockefeller_guns + rockefeller_tractors + rockefeller_uniforms
    result = total_supplies
    return result

print(solution())