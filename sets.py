import sets

s1 = set(map(int, raw_input().split()))

s2 = set(map(int, raw_input().split()))

print len(s1)

x = 3

print x in s1

print x not in s2

print s1.issubset(s2)

print s1.issuperset(s2)

print s1.union(s2) #|||ly intersection, difference, symmetric_difference and copy works

for val in s1.intersection(s2):
    print val