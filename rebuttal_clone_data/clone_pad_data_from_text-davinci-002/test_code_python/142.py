def solution(): 
     """ A cleaning company produces two sanitizer sprays. One spray kills 50% of germs, and another spray kills 25% of germs. However, 5% of the germs they kill are the same ones. What percentage of germs would be left after using both sanitizer sprays together?"""
     one_spray_germs_killed = .5
     other_spray_germs_killed = .25
     
     both_sprays_germs_killed = one_spray_germs_killed + other_spray_germs_killed - (.05 * 2)
     
     percentage_left = 1 - both_sprays_germs_killed
     
     return percentage_left

print(solution())