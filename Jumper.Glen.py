import random


class Answers:
   def __init__(self):
       self.secretWords = ["ghostbusters", "goonies", "mandalorian", "spiderman", "gremlins", "thor, avengers"]
       self.wordCount = 7

   def getWords(self):
       i = random.randint(0, self.wordCount - 1)
       return self.secretWords[i]

class Display:
   def getUserGuess(self):
       letter = input("Guess a letter [a-z]: ")
       return letter


class Skydiver:
   def __init__(self):
       self.skydiver = [" ___ ",
                    "/___\ ",
                      "\   / ",
                      " \ / ",
                       "  O ",
                      " /|\ ",
                      " / \ ",
                    "          ",
                    "^^^^^^^^^^",
                        "  ",
                     ""]


   def picture(self):
       for line in self.skydiver:
           print(line)

   def cutLine(self):
       self.skydiver = self.skydiver[1:]
       if len(self.skydiver) == 5:
           self.skydiver[0] = " RIP ";

   def gameOver(self):
       if len(self.skydiver) == 5:
           return True
       else:
           return False


class Puzzle:
   def __init__(self):
       self.words = Answers()
       self.console = Display()
       self.jumper = Skydiver()

       self.word = self.words.getWords()
       self.guess = ""


       for i in range(len(self.word)):
           self.guess += "-" 
       self.finished = False

   def playGame(self):
       print("\n" + self.guess)
       self.jumper.picture()
       if not self.finished:
           guessLetter = self.console.getUserGuess()
           incorrect = self.updateGuess(guessLetter)
           if not incorrect:
               self.jumper.cutLine() 


   def updateGuess(self, guessLetter):
       changed = False
       for i in range(len(self.word)):
           if self.word[i] == guessLetter and self.guess[i] == "-":
               self.guess = self.guess[0:i] + guessLetter + self.guess[i + 1:]
               changed = True
       return changed


   def isFinished(self):
       self.finished = True
       for i in range(len(self.guess)):
           if self.guess[i] == '-':
               self.finished = False
       if self.finished or self.jumper.gameOver():


           self.finished = True
           return True
       else:
           return False


   def results(self):
       print("The Answer is: " + self.word)
       print()

game = Puzzle()

while not game.isFinished(): 
   game.playGame()

game.playGame()
game.results()  

