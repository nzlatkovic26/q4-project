TV = [" $200", " $400", " $600", " $800", "$1000"]
MUSIC = [" $200", " $400", " $600", " $800", "$1000"]
GEO = [" $200", " $400", " $600", " $800", "$1000"]
FOOD_AND_DRINK = [" $200", " $400", " $600", " $800", "$1000"]
HISTORY = [" $200", " $400", " $600", " $800", "$1000"]
MOVIES = [" $200", " $400", " $600", " $800", "$1000"]

def board():
  print("                          FOOD                   ")
  print("   TV     MUSIC    GEO      &    HISTORY  MOVIES ")
  print("                          DRINK                  ")

  for i in range(0, len(TV)):
    print(f"|-------|-------|-------|-------|-------|-------|")
    print(f"| {TV[i]} | {MUSIC[i]} | {GEO[i]} | {FOOD_AND_DRINK[i]} | {HISTORY[i]} | {MOVIES[i]} |")
    
  print(f"|-------|-------|-------|-------|-------|-------|\n")

def twotv():
  return "This long-running animated series follows the adventures of a dysfunctional family living in the fictional town of Springfield."
  

def fourtv():
  return "In this popular sitcom, a group of friends living in New York City navigates the ups and downs of their careers, relationships, and personal lives."

def sixtv():
  return "In this acclaimed drama series, set in the 1960s, advertising executives at a Madison Avenue firm grapple with personal and professional challenges amidst the changing social landscape of America."


def eighttv():
  return "This dystopian drama series, based on Margaret Atwood's novel, depicts a society where fertile women are forced into reproductive servitude."
 

def tentv():
  return "In this critically acclaimed crime drama, set in Baltimore, Maryland, viewers follow the lives of both law enforcement officers and drug dealers as they navigate the city's complex social and political landscape."

def twomusic():
  return "This Canadian rapper is known for hits like 'Hotline Bling' and 'God's Plan'."

def fourmusic():
  return "This former child star from 'Dance Moms' has recently gained popularity for her poor dancing and singing skills."

def sixmusic():
  return "This legendary British rock band's iconic album 'The Dark Side of the Moon' spent a record-breaking 741 consecutive weeks on the Billboard 200 chart."

def eightmusic():
  return "This influential American rapper and actor released the album 'The Chronic' in 1992, which is considered one of the greatest hip-hop albums of all time."

def tenmusic():
  return "This iconic pop star's album 'Thriller' remains the best-selling album of all time, with over 66 million copies sold worldwide."

def twogeo():
  return "This river, the longest in the world, flows northward through northeastern Africa."

def fourgeo():
  return "This country is home to the world's largest tropical rainforest, covering much of its northern region."

def sixgeo():
  return "This mountain range, stretching approximately 4,350 miles across eight countries in South America, is the longest continental mountain range in the world."

def eightgeo():
  return "This European city, often called 'The Eternal City,' is home to landmarks such as the Colosseum, Vatican City, and the Trevi Fountain."

def tengeo():
  return "This country, located in the Horn of Africa, is the only nation in Africa that has never been colonized."

def twofood():
  return "This Italian dish features thin slices of beef, topped with a mixture of Parmesan cheese, arugula, and a squeeze of lemon."

def fourfood():
  return "This popular Mexican dish consists of a tortilla filled with various ingredients such as meat, beans, cheese, and vegetables, then folded and typically grilled or toasted."

def sixfood():
  return "This fermented tea beverage originated in China and is known for its potential health benefits, including probiotics and antioxidants."

def eightfood():
  return "This popular Japanese dish consists of vinegared rice served with a variety of ingredients such as raw or cooked fish, vegetables, and sometimes tropical fruits."

def tenfood():
  return "This French dish, consisting of thinly sliced potatoes, cream, garlic, and cheese, is typically baked until golden and bubbly."

def twohist():
  return "This European conflict, lasting from 1914 to 1918, involved many of the world's great powers and is often referred to as the 'Great War'."

def fourhist():
  return "In 1492, this Italian explorer, sailing under the flag of Spain, reached the Americas, opening the Age of Exploration."

def sixhist():
  return "This influential document, signed in 1215, limited the powers of the English monarchy and is considered a cornerstone of modern constitutional law."

def eighthist():
  return "This series of military and political conflicts, lasting from 1337 to 1453, saw the kingdoms of England and France battling over control of the French throne."

def tenhist():
  return "This ancient civilization, which flourished along the banks of the Tigris and Euphrates rivers, is credited with the invention of writing and the first known legal code, Hammurabi's Code."

def twomovies():
  return "In this classic film, a young girl named Dorothy is swept away to the magical land of Oz, where she encounters memorable characters such as the Scarecrow, Tin Man, and Cowardly Lion."

def fourmovies():
  return "In this 1994 Disney animated film, a young lion prince named Simba learns about responsibility and identity after the death of his father, Mufasa."

def sixmovies():
  return "In this Quentin Tarantino film, two hitmen, Jules Winnfield and Vincent Vega, navigate the Los Angeles criminal underworld while embarking on a series of interconnected stories."

def eightmovies():
  return "This epic fantasy film trilogy, directed by Peter Jackson and based on the novels by J.R.R. Tolkien, follows the journey of a young hobbit named Frodo Baggins as he sets out to destroy a powerful ring."

def tennmovies():
  return "In this 1991 film directed by Jonathan Demme, an FBI trainee named Clarice Starling seeks the help of imprisoned serial killer Hannibal Lecter to catch another serial killer known as Buffalo Bill."

print("")

def category(player_name):
  
  choose = input(f"Player {player_name} - Choose a category and price: ")
  if choose == 'TV $200':
    if TV[0] == " XXXX":
      print("This category has already been answered")
      return
    else: 
      print("")
      print(twotv())
  if choose == 'TV $400':
    if TV[1] == " XXXX":
      print("This category has already been answered")
      return
    else:
      print("")
      print(fourtv())
  if choose == 'TV $600':
    if TV[2] == " XXXX":
      print("This category has already been answered")
      return
    else:
      print("")
      print(sixtv())
  if choose == 'TV $800':
    if TV[3] == " XXXX":
      print("This category has already been answered")
      return
    else:
      print("")
      print(eighttv())
  if choose == 'TV $1000':
    if TV[4] == " XXXX":
      print("This category has already been answered")
      return
    else:
      print("")
      print(tentv())
  if choose == 'MUSIC $200':
    if MUSIC[0] == " XXXX":
      print("This category has already been answered")
      return
    else:
      print("")
      print(twomusic())
  if choose == 'MUSIC $400':
    if MUSIC[1] == " XXXX":
      print("This category has already been answered")
      return
    else:
      print("")
      print(fourmusic())
  if choose == 'MUSIC $600':
    if MUSIC[2] == " XXXX":
      print("This category has already been answered")
      return
    else:
      print("")
      print(sixmusic())
  if choose == 'MUSIC $800':
    if MUSIC[3] == " XXXX":
      print("This category has already been answered")
      return
    else:
      print("")
      print(eightmusic())
  if choose == 'MUSIC $1000':
    if MUSIC[4] == " XXXX":
      print("This category has already been answered")
      return
    else:
      print("")
      print(tenmusic())
  if choose == 'GEO $200':
    if GEO[0] == " XXXX":
      print("This category has already been answered")
      return
    else:
      print("")
      print(twogeo())
  if choose == 'GEO $400':
    if GEO[1] == " XXXX":
      print("This category has already been answered")
      return
    else:
      print("")
      print(fourgeo())
  if choose == 'GEO $600':
    if GEO[2] == " XXXX":
      print("This category has already been answered")
      return
    else:
      print("")
      print(sixgeo())
  if choose == 'GEO $800':
    if GEO[3] == " XXXX":
      print("This category has already been answered")
      return
    else:
      print("")
      print(eightgeo())
  if choose == 'GEO $1000':
    if GEO[4] == " XXXX":
      print("This category has already been answered")
      return
    else:
      print("")
      print(tengeo())
  if choose == 'FOOD & DRINK $200':
    if FOOD_AND_DRINK[0] == " XXXX":
      print("This category has already been answered")
      return
    else:
      print("")
      print(twofood())
  if choose == 'FOOD & DRINK $400':
    if FOOD_AND_DRINK[1] == " XXXX":
      print("This category has already been answered")
      return
    else:
      print("")
      print(fourfood())
  if choose == 'FOOD & DRINK $600':
    if FOOD_AND_DRINK[2] == " XXXX":
      print("This category has already been answered")
      return
    else:
      print("")
      print(sixfood())
  if choose == 'FOOD & DRINK $800':
    if FOOD_AND_DRINK[3] == " XXXX":
      print("This category has already been answered")
      return
    else:
      print("")
      print(eightfood())
  if choose == 'FOOD & DRINK $1000':
    if FOOD_AND_DRINK[4] == " XXXX":
      print("This category has already been answered")
      return
    else:
      print("")
      print(tenfood())
  if choose =="HISTORY $200":
    if HISTORY[0] == " XXXX":
      print("This category has already been answered")
      return
    else:
      print("")
      print(twohist())
  if choose == 'HISTORY $400':
    if HISTORY[1] == " XXXX":
      print("This category has already been answered")
      return
    else:
      print("")
      print(fourhist())
  if choose == 'HISTORY $600':
    if HISTORY[2] == " XXXX":
      print("This category has already been answered")
      return
    else:
    print("")
    print(sixhist())
  if choose == 'HISTORY $800':
    if HISTORY[3] == " XXXX":
      print("This category has already been answered")
      return
    else:
    print("")
    print(eighthist())
  if choose == 'HISTORY $1000':
    if HISTORY[4] == " XXXX":
      print("This category has already been answered")
      return
    else:
      print("")
      print(tenhist())
  if choose == 'MOVIES $200':
    if MOVIES[0] == " XXXX":
      print("This category has already been answered")
      return
    else:
      print("")
      print(twomovies())
  if choose == 'MOVIES $400':
    if MOVIES[1] == " XXXX":
      print("This category has already been answered")
      return
    else:
      print("")
      print(fourmovies())
  if choose == 'MOVIES $600':
    if MOVIES[2] == " XXXX":
      print("This category has already been answered")
      return
    else:
      print("")
      print(sixmovies())
  if choose == 'MOVIES $800':
    if MOVIES[3] == " XXXX":
      print("This category has already been answered")
      return
    else:
      print("")
      print(eightmovies())
  if choose == 'MOVIES $1000':
    if MOVIES[4] == " XXXX":
      print("This category has already been answered")
      return
    else:
      print("")
      print(tenmovies())

  return choose

def answers(player_name, choose):
  question = input(f"Player {player_name} - What is your question?: ")
  value = 0
    if choose == 'TV $200':
    value = 200
    if question != "What is the Simpsons?":
      value = -200
    else: 
      TV[0] = " XXXX"
  if choose == 'TV $400':
    value = 400
    if question != "What is Friends?":
      value = -400
    else: 
      TV[1] = " XXXX"
  if choose == 'TV $600':
    value = 600
    if question != "What is Mad Men?":
      value = -600
    else: 
      TV[2] = " XXXX"
  if choose == 'TV $800':
    value = 800
    if question != "What is Handmaid's Tale?":
       value = -800
    else: 
       TV[3] = " XXXX"
  if choose == 'TV $1000':
    value = 10000
    if question != "What is We Own This City?":
      value = -10000
    else: 
      TV[4] = " XXXX"
  if choose == 'MUSIC $200':
    value = 200
    if question != "Who is Drake?":
      value = -200
    else: 
      MUSIC[0] = " XXXX"
  if choose == 'MUSIC $400':
    value = 400
    if question != "Who is Elvis Presley?":
      value = -400
    else: 
      MUSIC[1] = " XXXX"
  if choose == 'MUSIC $600':
    value = 600
    if question != "Who is Pink Floyd?":
      value = -600
    else: 
      MUSIC[2] = " XXXX"
  if choose == 'MUSIC $800':
    value = 800
    if question != "Who is Dr. Dre?":
      value = -800
    else: 
      MUSIC[3] = " XXXX"
  if choose == 'MUSIC $1000':
    value = 10000
    if question != "Who is Michael Jackson?":
      value = -10000
    else: 
      MUSIC[4] = " XXXX"
  if choose == 'GEO $200':
    value = 200
    if question != "What is the Nile River?":
      value = -200
    else: 
      GEO[0] = " XXXX"
  if choose == 'GEO $400':
    value = 400
    if question != "What is the Brazil?":
      value = -400
    else: 
      GEO[1] = " XXXX"
  if choose == 'GEO $600':
    value = 600
    if question != "What are the Andes Mountains?":
      value = -600
    else: 
      GEO[2] = " XXXX"
  if choose == 'GEO $800':
    value = 800
    if question != "What is Rome?":
      value = -800
    else: 
      GEO[3] = " XXXX"
  if choose == 'GEO $1000':
    value = 1000
    if question != "What is Etheopia?":
      value = -1000
    else: 
      GEO[4] = " XXXX"
  if choose == 'FOOD AND DRINK $200':
    value = 200
    if question != "What is Carpaccio?":
      value = -200
    else: 
      FOOD_AND_DRINK[0] = " XXXX"
  if choose == 'FOOD AND DRINK $400':
    value = 400
    if question != "What are Tacos?":
      value = -400
    else: 
      FOOD_AND_DRINK[1] = " XXXX"
  if choose == 'FOOD AND DRINK $600':
    value = 600
    if question != "What is Kombucha?":
      value = -600
    else: 
      FOOD_AND_DRINK[2] = " XXXX"
  if choose == 'FOOD AND DRINK $800':
    value = 800
    if question != "What is Sushi?":
      value = -200
    else: 
      FOOD_AND_DRINK[3] = " XXXX"
  if choose == 'FOOD AND DRINK $1000':
    value = 1000
    if question != "What is Dauphinoise?":
      value = -1000
    else: 
      FOOD_AND_DRINK[4] = " XXXX"
  if choose == 'HISTORY $200':
    value = 200
    if question != "What was WW1?":
      value = -200
    else: 
      HISTORY[0] = " XXXX"
  if choose == 'HISTORY $400':
    value = 400
    if question != "Who was Christopher Colombus?":
      value = -400
    else: 
      HISTORY[1] = " XXXX"
  if choose == 'HISTORY $600':
    value = 600
    if question != "What was the Magna Carta?":
      value = -600
    else: 
      HISTORY[2] = " XXXX"
  if choose == 'HISTORY $800':
    value = 800
    if question != "What was the Hundred Years War?":
      value = -800
    else: 
      HISTORY[3] = " XXXX"
  if choose == 'HISTORY $1000':
    value = 1000
    if question != "Who were Sumerians?":
      value = -1000
    else: 
      HISTORY[0] = " XXXX"
  if choose == 'MOVIES $200':
    value = 200
    if question != "What is the Wizard of Oz?":
      value = -200
    else: 
      MOVIES[0] = " XXXX"
  if choose == 'MOVIES $400':
    value = 400
    if question != "What is The Lion King?":
      value = -400
    else: 
      MOVIES[1] = " XXXX"
  if choose == 'MOVIES $600':
    value = 600
    if question != "What is Pulp Fiction?":
      value = -600
    else: 
      MOVIES[2] = " XXXX"
  if choose == 'MOVIES $800':
    value = 800
    if question != "What is The Lord of the Rings?":
      value = -800
    else: 
      MOVIES[3] = " XXXX"
  if choose == 'MOVIES $1000':
    value = 1000
    if question != "What is Silence of the Lambs?":
      value = -1000
    else: 
      MOVIES[4] = " XXXX"
    return value

def play_game():
  players = {"A" : 0, "B" : 0, "C" : 0}
  print("Welcome to Jeopardy!")

  while(True):
    for name, value in players.items():
      board()
      choose = category(name)
      value = answers(name, choose)
      players[name] += value
      print(f"Player {name} score = ${players[name]}")
      
      
  
play_game()

categories = [ TV, MUSIC, GEO, FOOD_AND_DRINK, HISTORY, MOVIES ]
done = True 
for choose in categories:
  for value in choose:
    if value != " XXXX":
      done = False

if players["A"] > players["B"] and players["C"]:
  print("Player A wins!")
elif players["B"] > players["A"] and players["C"]:
  print("Player B wins!")
else:
  print("Player C wins!")

# 1: questions to all the answers
# 2: way to end the game (when all categories are finished)
# 3: way for multiple players to respond to the same answer
# 4: declare a winner with banner
