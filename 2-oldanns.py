# simple logical computation

# logical computations assuming that a neuron is activated when at least two of its inputs are active.

# C=A case
# a--> c-->
# '    ^
# '-->-'
a = 1
sum = a+a
y = 0
if sum >= 2:
    y = 1
else:
    y = 0

print("In case of C = A :> ",y)


# C= A ^ B
a = 1
b = 1
sum = 1+1

c = 0
if sum >=2:
    c = 1
else:
    c = 0

print("In case of C = A /\ B :> ",c)


# C = A \/ B
a = 1
b = 1
sum = a+a+b+b
c = 0
if sum >=2:
    c = 1
else:
    c = 0

print("In case of C = A \/ B :> ",c)

# C = A \/ B
a = 1
b = 1
sum = a+a-b
c = 0
if sum >=2:
    c = 1
else:
    c = 0

print("In case of C = A /\ B' :> ",c)
