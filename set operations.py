''' A set is a collection which is unordered, unindexed, and contains only unique elements.
Mutability:
the set itself is mutable - you can add remove elements.'''

#creating two sets
set1 = {1, 2, 3, 4, 5}
set2 = {4, 5, 6, 7, 8}

print("Union:", set1 | set2)

print(" intersection:", set1 & set2)

print("Difference (set1 - set2):", set1 - set2)

print("symmetric Difference:", set1 ^ set2)
