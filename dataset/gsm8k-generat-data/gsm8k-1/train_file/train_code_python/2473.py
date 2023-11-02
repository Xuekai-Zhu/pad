def solution():
    """Nissa is calculating a jail sentence for a man who was convicted of burglary. The base sentence is 1 year of jail for every $5,000 of goods stolen. The burglar is going to have his sentence length increased by 25% because this is his third offense, plus 2 additional years for resisting arrest. How many years total is the burglar's sentence if he stole $40,000 worth of goods?"""
    goods_stolen = 40000
    base_sentence_years = goods_stolen / 5000
    increased_sentence_years = base_sentence_years * 1.25
    total_sentence_years = increased_sentence_years + 2
    result = total_sentence_years
    return result

print(solution())