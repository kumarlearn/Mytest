import random
print (random.randint(0,9))


from random import randint
print(randint(0, 9))

nums = [x for x in range(10)]
random.shuffle(nums)
print nums
