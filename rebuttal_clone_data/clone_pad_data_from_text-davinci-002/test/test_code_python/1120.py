def solution():
     Jackson_investment = 500
     Brandon_investment = 500
     Jackson_change = Jackson_investment * 4
     Brandon_change = Brandon_investment * 0.2
     Jackson_total = Jackson_investment + Jackson_change
     Brandon_total = Brandon_investment + Brandon_change
     result = Jackson_total - Brandon_total
     return result

print(solution())