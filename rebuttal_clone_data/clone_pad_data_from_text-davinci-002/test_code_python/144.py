def solution():
     """The owner of a Turkish restaurant wanted to prepare traditional dishes for an upcoming celebration. She ordered ground beef, in four-pound packages, from three different butchers. The following morning, the first butcher delivered 10 packages. A couple of hours later, 7 packages arrived from the second butcher. Finally, the third butcher’s delivery arrived at dusk. If all the ground beef delivered by the three butchers weighed 100 pounds, how many packages did the third butcher deliver?"""
     first_delivery = 10
     second_delivery = 7
     third_delivery = 100 - (first_delivery + second_delivery)
     result = third_delivery
     return result

print(solution())