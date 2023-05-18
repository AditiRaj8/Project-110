import random
print(dir(random))
def counter(response):
    while response=="y":
        no=random.randint(1,6)
    if no==1:
        print("[-----]")
        print("[     ]")
        print("[  0  ]")
        print("[     ]")
        print("[-----]")