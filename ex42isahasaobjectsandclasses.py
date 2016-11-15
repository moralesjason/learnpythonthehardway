#!/usr/bin/env python

## Animal is-a object (yes, sort of confusing) look at the extra credit
class Animal(object):
	pass

## Dog is-a Animal is-a object
class Dog(Animal):
	
	def __init__(self, name):
		## init method of Dog. Set it's name.
		self.name = name

## Cat is-a Animal is-a object
class Cat(Animal):
	
	def __init__(self, name):
		## init method of Cat. Set it's name.
		self.name = name		

## Person is-a object
class Person(object):
	
	def __init__(self, name):
		## init method of Person. Set it's name.
		self.name = name

		## Person has-a pet of some kind
		self.pet = None

## Employee is-a Person
class Employee(Person):
	
	def __init__(self, name, salary):
		## ?? hmm what is this strange magic?
		super(Employee, self).__init__(name)
		## Employee has-a salary
		self.salary = salary

## Fish is-a object
class Fish(object):
	pass

## Salmon is-a Fish is-a object
class Salmon(Fish):
	pass

## Halibut is-a Fish is-a object
class Halibut(Fish):
	pass


## rover is-a Dog
rover = Dog("Rover")

## satan is-a Cat
satan = Cat("Satan")

## mary is-a Person
mary = Person("Mary")

## mary has-a pet satan is-a Cat
mary.pet = satan

## frank is-a Person
frank = Employee("Frank",120000)

## frank has-a pet rovet is-a Dog
frank.pet = rover

## flipper is-a Fish
flipper = Fish()

## crouse is-a Salmon
crouse = Salmon()

## harry is-a Halibut()
harry = Halibut()





		
