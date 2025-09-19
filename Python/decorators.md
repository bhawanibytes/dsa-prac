There 3 type of Decorators -
- Function Decorators => behaves like high order function
- Class Decorators => behaves like high order function but for class cause take they class as input instead of function and can return same class or modified one.
- Method Decorators => These are usally built-ins and applied on functions defined in class
  Ex. @staticmethod => run without input of self
  @classmethod => receives input of class instead of self(instance)
  @property => turns method in attributes like getters and setterd; and even called without actual parentheses calls