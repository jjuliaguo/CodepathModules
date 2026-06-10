#Problem 3: T-I-Double Guh-Er II
#T-I-Double Guh-Er: That spells Tigger! 
# Write a function tiggerfy() that accepts a string word and returns a new string 
# that removes any substrings t, i, gg, and er from word. The function should be case insensitive.

def tiggerfy(word):
	#You don't actually need a for loop
	#TO DO: understand the replace()
	
	changed = word.lower()
	changed = changed.replace("t", "")
	changed = changed.replace("i", "")
	changed = changed.replace("gg", "")
	changed = changed.replace("er", "")
	return changed

#Previous solution

"""
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
	"""
   
#Example Usage:

word = "Trigger"
print(tiggerfy(word))

word = "eggplant"
print(tiggerfy(word))

word = "Choir"
print(tiggerfy(word))
#Example Output:

#"r"
#"eplan"
#"chor"