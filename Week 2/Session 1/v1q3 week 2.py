#Question 3
# 
# Captain Blackbeard has an integer array chests of length n where all 
# the integers in chests are in the range [1, n] and each integer appears 
# once or twice. Return an array of all the integers that appear twice, 
# representing the treasure chests that have duplicates.

def find_duplicate_chests(chests):

    duplicates = []
    tempSet = set()

    for ind in chests:
        if ind in tempSet:
            duplicates.append(ind)
        else:
            tempSet.add(ind)
    return duplicates
   
    """
    
    frequencies = {}

    for key in chests:
        if key in frequencies:
            frequencies[key] += 1
        else:
            frequencies[key] = 1

    """
        

#Example Usage:

chests1 = [4, 3, 2, 7, 8, 2, 3, 1]
chests2 = [1, 1, 2]
chests3 = [1]

print(find_duplicate_chests(chests1))
print(find_duplicate_chests(chests2))
print(find_duplicate_chests(chests3))

"""
Example Output:

[2, 3]
[1]
[]
"""