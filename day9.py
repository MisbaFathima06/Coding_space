programming_dictionary= {
    "Function": "A reusable block of code that performs a specific task. You call it when needed.",
    "Loop": "Repeats a set of instructions until a condition is met (e.g., for, while).",
    "List": "A collection of items that can change. Ordered, mutable, and uses square brackets [].",
}

# to retrieve a word
print(programming_dictionary["Loop"])

#to add a word
programming_dictionary["Tuple"]="A collection of items that cannot change. Ordered, immutable, and uses parentheses ()."


# to wipe anexisting dictionary
programming_dictionary={}

# to edit item in dictionary
programming_dictionary["Loop"]="It repeats a task again and again until a condition is met"
print(programming_dictionary)


#loop through dictionary

for key in programming_dictionary:
    print(key)
    print(programming_dictionary[key])

starting_dictionary = {
    "a": 9,
    "b": 8,
}


final_dictionary = {
    "a": 9,
    "b": 8,
    "c": 7,
}


