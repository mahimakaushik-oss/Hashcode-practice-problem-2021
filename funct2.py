# -*- coding: utf-8 -*-
"""
Created on Mon Feb 22 20:33:09 2021

@author: Mahima Kaushik
"""

from tqdm import tqdm 
import functools 

global sub_file
global final_file
final_file=[]
        
def f1_in(path):
    f = open(path,"r")
    global lines_in_file 
    lines_in_file =[]
    global final_raw
    final_raw=[]
    for line in f:
        each_line = line.strip()      #getting file
        line_list = each_line.split()
        lines_in_file.append(line_list)
    
    final_raw= [(idx, item) for idx,item in enumerate(lines_in_file[1:])]
    
    
         

def compare():
    global path
    path=input("enter file name: ")
    f1_in(path)
    global modify_lines
    modify_lines = sorted(final_raw, key = lambda x: len(x[1]),reverse=True)  #sorting a file
    global factors
    factors=[int(i) for i in lines_in_file[0]] 
    for i in modify_lines:
        print(i)
    #zeroth row
   
    #selection() 
    #get_pizza()
    #distribute(4)
   
    
    
                                            
def selection():
    pizza_box=[]
    total_pizza=factors[0]                         
    max_inge = (max(map(len,modify_lines)))        #total of 4 files is 18,50,49,317.
    inge=[]                                        #74 example
    for i in tqdm(modify_lines):                  #8397 little bit
        if len(i) == max_inge:                    #1853388 many_pizzas
            print(i)                               #183187458 many_ingredients
            inge.append(i)                  #analysing the files
    print(len(inge))
    no_of_inge = tqdm(functools.reduce(lambda a,b:a+b,inge))
    #print(set(no_of_inge))
    #print(len(set(no_of_inge)))
    
            
        
def get_pizza():
    global members
       #give 3 if to test a_example
    global score
    global count
    score=0
    count=0
    m=4
    for i in [factors[3],factors[2],factors[1]]:
        
        for j in range(i):
            sub_file=[]
            count=count+1
            distribute(m)
            score = score+p_score
        m=m-1
    #print(len(modify_lines))
    print(score)
            
            
def distribute(members):
    pizzas=[]
    global p_score
    p_score=0
    global sub_file
    sub_file=[members]
    
    for m in range(members):
        if m==0 or m==1 or m==2 or m==3:
            pizzas.append(final_pizzas[0][1][1:])    #preparing pizzas box and remove those from table
            sub_file.append(final_pizzas[0][0])
            final_pizzas.pop(0)
        else:
            pizzas.append(final_pizzas[-1][1][1:])
            sub_file.append(final_pizzas[-1][0])
            final_pizzas.pop(-1)
    final_file.append(sub_file)
    
    #print(pizzas)
    #print(len(set(functools.reduce(lambda a,b:a+b,pizzas))))
    p_score=(len(set(functools.reduce(lambda a,b:a+b,pizzas))))**2
    

def proper_deal():

    compare()
    global final_pizzas
    final_pizzas=[]
    all_team=factors[1]*2+ factors[2]*3+ factors[3]*4       # getting pizza where number
    if factors[0]>=(all_team):                              #number of total memebers
        final_pizzas = modify_lines[0:all_team]             # are less than or equal to
        get_pizza()
    else:
        final_pizzas= sorted(modify_lines,key=len, reverse= False)
        choice()
    if factors[1]+factors[2]+factors[3]==4:
        smallfile()
    get_output()
                                                            #total pizzas

        
def choice():
    mem=0
    inc=0
    score=0
    global count
    count=0
    four = factors[3]
    three= factors[2]
    two= factors[1]
    dis = {
        1: 4,
        2:3,
        3: 2
        }

    
    n=1
    for i in [four,three,two]:
        mem=dis.get(n)
        for j in range(1,i+1):
            if (j*mem < factors[0]) or (j*mem == factors[0]):
                inc=inc+1
        
        factors[0]=factors[0]-inc*mem
        if factors[0]!=1:
            for ex in range(inc):
                count=count+1
                distribute(mem)
                score=score+p_score
            
            inc=0

        elif factors[0]==1:
            factors[0]=factors[0]+inc*mem
            inc=0
            continue
        n=n+1
    print(score)
    
def smallfile():
    mem=0
    inc=0
    score=0
    global count
    count=0
    four = factors[3]
    three= factors[2]
    two= factors[1]
    dis = {
        1: 3,
        2:4,
        3: 2
        }

    
    n=1
    for i in [three,two,four]:
        mem=dis.get(n)
        for j in range(1,i+1):
            if (j*mem < factors[0]) or (j*mem == factors[0]):
                inc=inc+1
        
        factors[0]=factors[0]-inc*mem
        if factors[0]!=1:
            for ex in range(inc):
                count=count+1
                distribute(mem)
                score=score+p_score
            
            inc=0

        elif factors[0]==1:
            factors[0]=factors[0]+inc*mem
            inc=0
            continue
        n=n+1
    
    
                
        
            
    
    
def get_output():
    with open(path+'.out', 'w') as f:
        f.write(str(count)+"\n")
        for i in final_file:
            f.write(" ".join(str(x) for x in i)+"\n")
        
        
        
        
        
            
          
proper_deal()