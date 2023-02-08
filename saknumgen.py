import random

def make_list():
    number = (random.randrange(9999999))
    end = (random.randrange(9999))
    result = (number, "0", "A", end)
    print (''.join(map(str, result)))

for gen in range(99999):
    make_list()
