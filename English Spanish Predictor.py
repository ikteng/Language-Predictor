import math
import string

def get_parameter_vectors():
    '''
    This function parses e.txt and s.txt to get the  26-dimensional multinomial
    parameter vector (characters probabilities of English and Spanish) as
    descibed in section 1.2 of the writeup

    Returns: tuple of vectors e and s
    '''
    #Implementing vectors e,s as lists (arrays) of length 26
    #with p[0] being the probability of 'A' and so on
    e=[0]*26
    s=[0]*26

    with open('e.txt',encoding='utf-8') as f:
        for line in f:
            #strip: removes the newline character
            #split: split the string on space character
            char,prob=line.strip().split(" ")
            #ord('E') gives the ASCII (integer) value of character 'E'
            #we then subtract it from 'A' to give array index
            #This way 'A' gets index 0 and 'Z' gets index 25.
            e[ord(char)-ord('A')]=float(prob)
    f.close()

    with open('s.txt',encoding='utf-8') as f:
        for line in f:
            char,prob=line.strip().split(" ")
            s[ord(char)-ord('A')]=float(prob)
    f.close()

    return (e,s)

def shred(filename):
  #Using a dictionary here. You may change this to any data structure of
  #your choice such as lists (X=[]) etc. for the assignment
  X=dict()
  with open (filename+".txt",encoding='utf-8') as f:
    file1=f.read().upper()
  for c in string.ascii_uppercase: 
    X[c]=0
  for c in file1:
    if (c not in string.ascii_uppercase):
      continue
    else:
      X[c]+=1
    
  #print(X)
      
  return X

def F_Y(X):
   sum_XiE=0
   sum_XiS=0
   letters = list(string.ascii_uppercase) #list of the alphabets
   e,s=get_parameter_vectors()

   #P(Y=y)
   P_YE=0.6 #P(Y=english)
   P_YS=0.4 #P(Y=spanish)

   for i in range(len(letters)):
       #Xi_logPi
       Xi_logPiE=X[letters[i]]*math.log(e[i])
       Xi_logPiS=X[letters[i]]*math.log(s[i])

       sum_XiE+=Xi_logPiE
       sum_XiS+=Xi_logPiS 
    
   F_YE=math.log(P_YE) + sum_XiE
   F_YS=math.log(P_YS) + sum_XiS

   return (F_YE,F_YS)

def P_Y_XE(F_YE,F_YS):
    if (F_YS-F_YE)>=100:
       P_Y_XE=0
    elif (F_YS-F_YE)<=-100:
       P_Y_XE=1
    else:
       e_F=math.exp(F_YS-F_YE)
       P_Y_XE=1/(1+e_F)
    
    return P_Y_XE

#main method
if __name__=="__main__":
    #name of file that will be scanned
    filename="letter" 
    with open(filename+".txt") as f:
        print()
        #call shred method to shred the number of letters to number of alphabets
        s1=shred(filename) #X = number of alphabets
    # for c in string.ascii_uppercase:
    #     #print alphabet + number of times counted
    #     print(c +" "+str(s1[c]))
    
    #baysian_probability(s1)
    F_YE,F_YS=F_Y(s1)
    print("F(English) = {:.4f}\nF(Spanish) = {:.4f}\n".format(F_YE,F_YS))

    # probability of language being English given the number of alphabets
    P_Y_XE=P_Y_XE(F_YE,F_YS)
    print("P(Y = English|X) = {:.4f}\n".format(P_Y_XE))

    if(P_Y_XE==1 or P_Y_XE==0): 
    #not really possible to have a perfect percentage, could only mean that the program don't recognize the language
       print("The Language is neither English or Spanish\n")
    elif(P_Y_XE>0.5):
       print("The Language is most likely to be English\n")
    elif(P_Y_XE<0.5):
       print("The Language is most likely to be Spanish\n")
    

