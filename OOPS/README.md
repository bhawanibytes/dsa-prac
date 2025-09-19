#### Class => Blueprint => Done
#### Object => Real Instance => Done

#### Fundamental Concepts -
- Encapsulation (Data Hiding) => Done
- Inheritance (Reusability) 
- Polymorphism (Many Forms)
- Abstraction (Hiding Implementation)

#### Python Specifics =>
-  ##### __init__ is default function/method/magic_method in python class for initialization, __new__ is for constructor
-  ##### Double understore (__example) makes variable private by name mangled
-  ##### And Signle underscore (_example) makes it protected, not enforced
- ##### When child class redefines the Parent class methods, they are overriden in child class
- ##### in the case of private variable any method that mutates it called SETTER, setters must to do validations of data before doing any mutations
- ##### in the case of private variable any method that prints or returns its value is called GETTER