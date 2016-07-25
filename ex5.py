name = 'Yurii Bilousov'
age = 26 # not a lie
height = 72 #inches
weight = 172 # lbs
eyes = 'Green'
teeth = 'Yellow'
hair = 'Black'

print("Let's talk about %s." % name)
print("He's %d inches tall" % height)
print("He's %r pounds heavy" % weight)
print("Actually that's not too heavy.")
print("He's got %s eyes and %s hair" % (eyes, hair))
print("His teeth are usually %s depending on coffee" % teeth)

#this line is tricky try to get it exactly right
print("If I add %d, %d, and %d I get %d " % (
		age, height, weight, age + height + weight))