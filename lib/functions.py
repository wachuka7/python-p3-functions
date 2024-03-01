#!/usr/bin/env python3

def greet_programmer():
    print("Hello, programmer!")
greet_programmer()

def greet(name="programmer"):
    print(f'Hello, {name}!')
greet("Naureen")    

def greet_with_default(name="programmer"):
    print(f'Hello, {name}!')
greet_with_default()
greet_with_default("Sunny")


def add(num1, num2):
    print(num1+num2)
    return 45 + 55;


def halve(number):
    if not isinstance(number, (int, float)):
        return None
    print(number/2)
    return(100/2)
   
        
