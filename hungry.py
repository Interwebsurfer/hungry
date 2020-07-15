#im making this to decide what i should eat
import random
 
meats = ["chicken", "turkey", "beef", "eggs", "no meat"]
sides = ["rice", "beans", "broccoli", "spinich", "salad"]
drinks = "water"

rand_meats = random.choice(meats)
rand_sides = random.choice(sides)


if rand_meats == "no meat":
    print("you should eat " + random.choice(sides) + " with " + rand_sides + " and drink some " + drinks)
else:
    print("you should eat " + rand_meats + " with " + rand_sides + " and drink some " + drinks)
