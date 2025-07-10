# Write code below 💖

class Restaurant: #Las clases son moldes o plantillas para usar mas adelante fuera o dentro del archivo
  name = ''
  type = ''
  rating = 0.0
  delivery = False

bobs_burguers = Restaurant()

bobs_burguers.name = "Felas"
bobs_burguers.category = "American Diner"
bobs_burguers.rating = 4.7
bobs_burguers.delivery = False

cocos = Restaurant()

cocos.name = "Cocos"
cocos.category = "Mexican Diner"
cocos.rating = 4.9
cocos.delivery = False

chilaquiles = Restaurant()

chilaquiles.name = "Chilaquiles"
chilaquiles.category = "Mexican Diner"
chilaquiles.rating = 5.0
chilaquiles.delivery = True

print(vars(bobs_burguers))
print(vars(cocos))
print(vars(chilaquiles)) 