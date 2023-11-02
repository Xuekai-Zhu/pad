def solution():
     beaded_necklaces = 10 + 2
     beaded_bracelets = 5
     beaded_earrings = 7
     beads_per_necklace = 20
     beads_per_bracelet = 10
     beads_per_earring = 5
     total_beads = beaded_necklaces * beads_per_necklace + beaded_bracelets * beads_per_bracelet + beaded_earrings * beads_per_earring
     result = total_beads
     return result

print(solution())