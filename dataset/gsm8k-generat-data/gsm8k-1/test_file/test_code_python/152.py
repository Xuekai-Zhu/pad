def solution():
    """The zookeeper feeds all the apes in the zoo. He orders all the bananas from a local farm every 2 months. If the monkeys need 200 bananas, the gorillas need 400 bananas, and the baboons need 100 bananas every month, how many bananas does he need to order to last for 2 months?"""
    bananas_per_monkey = 200
    monkeys = 1
    bananas_per_gorilla = 400
    gorillas = 1
    bananas_per_baboon = 100
    baboons = 1
    months = 2
    total_bananas = (bananas_per_monkey * monkeys + bananas_per_gorilla * gorillas + bananas_per_baboon * baboons) * months
    result = total_bananas
    return result

print(solution())