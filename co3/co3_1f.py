import random
random.seed(10)
print(random.random())
print(random.uniform(20, 60))
lst = ["orange", "apple", "graphes"]
print(random.sample(lst, k=2))
print(random.random())
lst2 = ["orange", "apple", "graphes"]
random.shuffle(lst2)
print(lst2)
lst3 = ["orange", "apple", "graphes"]
print(random.choice(lst3))