print("           POP            FOOD                   ")
print("   TV    CULTURE   GEO      &    HISTORY  MOVIES ")
print("                          DRINK                  ")
print("|-------|-------|-------|-------|-------|-------|")
print("| $200  | $200  | $200  | $200  | $200  | $200  |")
print("|-------|-------|-------|-------|-------|-------|")
print("| $400  | $400  | $400  | $400  | $400  | $400  |")
print("|-------|-------|-------|-------|-------|-------|")
print("| $600  | $600  | $600  | $600  | $600  | $600  |")
print("|-------|-------|-------|-------|-------|-------|")
print("| $800  | $800  | $800  | $800  | $800  | $800  |")
print("|-------|-------|-------|-------|-------|-------|")
print("| $1000 | $1000 | $1000 | $1000 | $1000 | $1000 |")
print("|-------|-------|-------|-------|-------|-------|")

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

def tenmovies():
  return "In this 1991 film directed by Jonathan Demme, an FBI trainee named Clarice Starling seeks the help of imprisoned serial killer Hannibal Lecter to catch another serial killer known as Buffalo Bill."

print("")

def category():
  choose = input("Choose a category and price: ")
  if choose == 'TV $200':
    print("")
    print(twotv())
  if choose == 'TV $400':
    print("")
    print(fourtv())
  if choose == 'TV $600':
    print("")
    print(sixtv())
  if choose == 'TV $800':
    print("")
    print(eighttv())
  if choose == 'TV $1000':
    print("")
    print(tentv())
  if choose == 'MUSIC $200':
    print("")
    print(twomusic())
  if choose == 'MUSIC $400':
    print("")
    print(fourmusic())
  if choose == 'MUSIC $600':
    print("")
    print(sixmusic())
  if choose == 'MUSIC $800':
    print("")
    print(eightmusic())
  if choose == 'MUSIC $1000':
    print("")
    print(tenmusic())
  if choose == 'GEO $200':
    print("")
    print(twogeo())
  if choose == 'GEO $400':
    print("")
    print(fourgeo())
  if choose == 'GEO $600':
    print("")
    print(sixgeo())
  if choose == 'GEO $800':
    print("")
    print(eightgeo())
  if choose == 'GEO $1000':
    print("")
    print(tengeo())
  if choose == 'FOOD & DRINK $200':
    print("")
    print(twofood())
  if choose == 'FOOD & DRINK $400':
    print("")
    print(fourfood())
  if choose == 'FOOD & DRINK $600':
    print("")
    print(sixfood())
  if choose == 'FOOD & DRINK $800':
    print("")
    print(eightfood())
  if choose == 'FOOD & DRINK $1000':
    print("")
    print(tenfood())
  if choose =="HISTORY $200":
    print("")
    print(twohist())
  if choose == 'HISTORY $400':
    print("")
    print(fourhist())
  if choose == 'HISTORY $600':
    print("")
    print(sixhist())
  if choose == 'HISTORY $800':
    print("")
    print(eighthist())
  if choose == 'HISTORY $1000':
    print("")
    print(tenhist())
  if choose == 'MOVIES $200':
    print("")
    print(twomovies())
  if choose == 'MOVIES $400':
    print("")
    print(fourmovies())
  if choose == 'MOVIES $600':
    print("")
    print(sixmovies())
  if choose == 'MOVIES $800':
    print("")
    print(eightmovies())
  if choose == 'MOVIES $1000':
    print("")
    print(tenmovies())
