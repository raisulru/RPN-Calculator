# RPN-Calculator
A Reverse Polish Notation Calculator in python.

# Running process
- Simply run into any console where python is available.
- Of course run with python3.
- After runing give input as a seperate value or only press enter to see the default input.

# Algorithm
- Used stack for store the RPN to infix converted result.
- Executed the final result using the final infix result.
- Printed out the both infix and calculation result.

# Implemention
- Used a main function for general python code.
- Created a calculator class with calculate method
- For operator operation used a factory pattern to access every operator individually.
- With this factory pattern you can override the interface method to extend the functionality.
- For new operation create a class into this pattern and add a object with its sign.