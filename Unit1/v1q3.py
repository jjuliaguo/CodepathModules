#Problem 3: T-I-Double Guh-Er II
#T-I-Double Guh-Er: That spells Tigger! 
# Write a function tiggerfy() that accepts a string word and returns a new string 
# that removes any substrings t, i, gg, and er from word. The function should be case insensitive.

def tiggerfy(word):
	changed = word.lower()
	for index in range(len(changed)):
        if changed[index] == "t":
            changed = changed.replace("t", "")
        elif changed[index] == "i":
            changed = changed.replace("i", "")
        elif changed[index:index+2] == "gg":
            changed = changed.replace("gg", "")
        elif changed[index:index+2] == "er":
            changed = changed.replace("er", "")
        else:
            continue
    return changed
#Example Usage:

word = "Trigger"
tiggerfy(word)

word = "eggplant"
tiggerfy(word)

word = "Choir"
tiggerfy(word)
#Example Output:

#"r"
#"eplan"
#"chor"