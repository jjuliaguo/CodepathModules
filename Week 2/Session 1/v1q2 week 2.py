#Question 2
# 
# Taken captive, Captain Anne Bonny has been smuggled a secret message 
# from her crew. She will know she can trust the message if it contains 
# all of the letters in the alphabet. Given a string message containing 
# only lowercase English letters and whitespace, 
# write a function can_trust_message() that returns True if the message 
# contains every letter of the English alphabet at least once, and False otherwise.

def can_trust_message(message):
    frequency = set(message)
    if len(frequency) == 27:
        return True
    else:
        return False

"""

    for key in message:
        if key in frequency:
            frequency[key] += 1
        else:
            frequency[key] = 1
        
        if key != " ":
            if frequency[key] == 0:
                return False
                
    if len(frequency) != 26:
        return False
    return True
"""

#Example Usage:

message1 = "sphinx of black quartz judge my vow"
message2 = "trust me"

print(can_trust_message(message1))
print(can_trust_message(message2))
"""
Example Output:

True
False
"""