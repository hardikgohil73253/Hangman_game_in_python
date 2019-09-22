#!/usr/bin/python3
# Hangman game
import random
class HangMan_Try3(object):

    # Hangman game
    hang = []
    hang.append(' +---+')
    hang.append(' |   |')
    hang.append('     |')
    hang.append('     |')
    hang.append('     |')
    hang.append('     |')
    hang.append('=======')

    array = {}
    array[0] = [' 0   |']
    array[1] = [' 0   |', ' |   |']
    array[2] = [' 0   |', '/|   |']
    array[3] = [' 0   |', '/|\\  |']
    array[4] = [' 0   |', '/|\\  |', '/    |']
    array[5] = [' 0   |', '/|\\  |', '/ \\  |']

    photos = []

    words = '''ant baboon badger bat bear beaver camel cat clam cobra cougar coyote
            crow deer dog donkey duck eagle ferret fox frog goat goose hawk lion lizard llama
            mole monkey moose mouse mule newt otter owl panda parrot pigeon python rabbit ram
            rat raven rhino salmon seal shark sheep skunk sloth snake spider stork swan tiger
            toad trout turkey turtle weasel whale wolf wombat zebra'''.split()

    infStr = '_-*\'*-_-*\'*-_-*\'*-_-*\'*-_-*\'*-_-*\'*-_-*\'*-_-*\'*-_-*\'*-_-*\''

    def __init__(self, *args, **kwargs):
        i, j = 2, 0
        self.photos.append(self.hang[:])
        for ls in self.array.values():
            pic, j = self.hang[:], 0
            for m in ls:
                pic[i + j] = m
                j += 1
            self.photos.append(pic)

    def pickWord(self):
        return self.words[random.randint(0, len(self.words) - 1)]

    def printPic(self, idx, wordLen):
        for line in self.photos[idx]:
            print(line)

    def askAndEvaluate(self, word, result, missed):
        guess = input()
        if guess == None or len(guess) != 1 or (guess in result) or (guess in missed):
            return None, False
        i = 0
        right = guess in word
        for c in word:
            if c == guess:
                result[i] = c
            i += 1
        return guess, right

    def info(self, info):
        ln = len(self.infStr)
        print(self.infStr[:-3])
        print(info)
        print(self.infStr[3:])

    def start(self):
        print('Welcome to Hangman !')
        word = list(self.pickWord())
        result = list('*' * len(word))
        print('The word is: ', result)
        success, i, missed = False, 0, []
        while i < len(self.photos)-1:
            print('Guess the word: ', end='')
            guess, right = self.askAndEvaluate(word, result, missed)
            if guess == None:
                print('You\'ve already entered this character.')
                continue
            print(''.join(result))
            if result == word:
                self.info('Congratulations ! You\'ve just saved Var life !')
                success = True
                break
            if not right:
                missed.append(guess)
                i += 1
            self.printPic(i, len(word))
            print('Missed characters: ', missed)

        if not success:
            self.info('The word was \''+''.join(word) +
                      '\' ! You\'ve just killed Var array, yo !')
Var = HangMan_Try3().start()
