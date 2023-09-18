'''Implemend a class called player that representsa cricket player.the player class should have a
method called play() which print "The player is playing cricket. Derive two classes, Batsman and 
Bowler, from the player class. override the play() method in each derived class to print " The batsman
is batting" and "The bowler is bowling", respectively.
Batsman and Bowler classes and call the play() method for each object.'''


#Define the base class player
class player:
  def play(self):
      print("The player cricket.")

#Define the derived class Batsman
class Batsman(player):
    def play(self):
        print("The batsman is batting.")

#Define the derived class Bowler
class Bowler(player):
    def play(self):
        print("The bowler is bowling.")

#Create objects of Batsman and Bowler classes
batsman = Batsman()
bowler = Bowler()

# Call the play() method for each object
batsman.play()
bowler.play()