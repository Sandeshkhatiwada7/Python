# Creating two sets
set1 = {10, 20, 30, 40, 50}
set2 = {40, 50, 60, 70, 80}

print("Set 1:", set1)
print("Set 2:", set2)
print("Length of Set 1:", len(set1))

set1.remove(20)
print("After removing 20 from Set 1:")
print(set1)

removed_element = set1.pop()
print("Popped element:", removed_element)
print("Set 1 after pop:", set1)

union_set = set1.union(set2)
print("Union of Set 1 and Set 2:")
print(union_set)

intersection_set = set1.intersection(set2)
print("Intersection of Set 1 and Set 2:")
print(intersection_set)

set1.clear()
print("Set 1 after clear():")
print(set1)