def solution():
    """Ahmed has 8 orange trees and four times as many apple trees in his orchard as Hassan. If Hassan has one apple tree and two orange trees, and they both have only apple and orange trees in their orchards, how many more trees are in Ahmed's orchard than in Hassan's?"""
    ahmed_oranges = 8
    hassan_apples = 1
    hassan_oranges = 2
    hassan_total = hassan_apples + hassan_oranges
    ahmed_apples = hassan_apples * 4
    ahmed_total = ahmed_oranges + ahmed_apples
    difference = ahmed_total - hassan_total
    result = difference
    return result

print(solution())