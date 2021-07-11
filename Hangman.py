#!/usr/bin/env python
# coding: utf-8

# In[18]:


from random import choice


# In[ ]:





# In[26]:


def word_generator():
    with open("wordlist.txt","r") as f:
        lines=f.readlines()
    f.close()
    lines=[i.strip("\n")for i in lines]
    return choice(lines)


# In[29]:


word=word_generator()
guessed= ""
turns=int(len(word)*1.5)
while(True):
    print("You are left with {} turns".format(turns))
    inp=input("Make a guess: ")
    turns=turns-1
    if inp in word:
         guessed=guessed+inp
    unguessed_char=0        
    for i in word:
        if i in guessed:
            print(i,end="")
        else:
            unguessed_char +=1
            print("*",end="")
    if unguessed_char ==0:
        print("\nHurray!! you won.....")
        break
    if turns==0:
        print("\nmy my my.....You ran out of attempts")
        break
        


# In[41]:


def get_hangman(index):
hangman=[
    """""""
    |---------------________
    |                  |
    |               
    |                  |
    |                
    |               
    |                 /     |,
    
    |---------------________
    |                  |
    |                 /     |                  |
    |                
    |                
    |                 /     |,
    
    |---------------________
    |                  |
    |                 / \ 
    |                  |
    |                
    |                \___/
    |                 /     |,
    
    |---------------________
    |                  |
    |                 /     |                  |
    |                /       |                \___/
    |                 /     |
    
]
return choice(hangman(index))


# In[ ]:





# In[ ]:




