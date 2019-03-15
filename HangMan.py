# -*- coding: utf-8 -*-
"""
Created on Wed Mar 13 14:57:31 2019

@author: Khin Khin Min Thu
"""
import random

class HangMan:
    score = 0    
    def __init__(self, category):
        self.word_list = self.loadFile(category)
        self.start_game()
   
    def start_game(self):     
        self.selected_word = 'acc' #self.pick_word() #word for player to guess
        self.display_letters = self.init_letters() #word player is guessing so far
        self.wrong_letters = [] #list of letter playered wrongly guessed
        self.win = False #True is player can guess the whole word correctly
        print('Game START', self.selected_word,self.display_letters ,  self.wrong_letters ,self.win)
        
    def pick_word(self):
        word = random.choice(self.word_list)
        print('Selected word: ', word, ', Len: ', len(word))
        
         #remove the selected word from the list
        self.word_list.remove(word)
        print('Removed word: ', word, ', Remaining words: ', len(self.word_list))
        return word
    
    def init_letters(self):
        #initialize the list with '_'
        letters = ['_'] * len(self.selected_word)
        print('Display letters: ', letters)
        return letters
        
    def loadFile(self, category):
        word_dir = 'words/'
        with open(word_dir+category+'.txt', 'r') as file:
            word_list = file.read().splitlines()
            
        #print('Total words loaded ('+category+'): ', len(word_list))
        return word_list
    
    def guess_letter(self, letter):
        indices = [i for i, char in enumerate(self.selected_word) if char == letter]
        
        if(len(indices) == 0):
            self.wrong_letters.append(letter)
        else:
            for i in indices:
                self.display_letters[i] = self.selected_word[i]
        print('-------------------------------------------------------------------')    
        print('Guessed letter: ', letter)
        print('Wrongly guessed letter: ', self.wrong_letters)
        print('Display letter: ', self.display_letters)
        self.check_win()
        print('-------------------------------------------------------------------')
        
    def check_win(self):
        #player has guessed the word correctly if there is no "_" in the list
        if not '_' in self.display_letters:
            self.win = True
            HangMan.score += 1
        print('Did player win?: ', self.win, HangMan.score)
        
    def display_word(self):
        display_word = " ".join(self.display_letters)
        return display_word
        
    def display_wrong_letters(self):
        display_wrong_letters = " ".join(self.wrong_letters)
        return display_wrong_letters
        
        
        
        
        
        
        
        
        
        
        