from pyswip import Prolog

# Initialize Prolog engine
prolog = Prolog()

# Knowledge base
# a. If something is food, John likes it
prolog.assertz("likes(john, X) :- food(X)")

# b. Apple and vegetables are food
prolog.assertz("food(apple)")
prolog.assertz("food(vegetables)")

# c. Anything someone eats and is not killed is food
prolog.assertz("food(Z) :- eats(Y, Z), not_killed(Y)")

# d. Anil eats peanuts
prolog.assertz("eats(anil, peanuts)")

# e. Anil is alive
prolog.assertz("alive(anil)")

# f. If someone is alive, they are not killed
prolog.assertz("not_killed(X) :- alive(X)")

# Query to prove: John likes peanuts
query = "likes(john, peanuts)"

# Check if the query can be proven
result = list(prolog.query(query))

# Output the result
if result:
    print("Proven: John likes peanuts.")
else:
    print("Cannot prove that John likes peanuts.")