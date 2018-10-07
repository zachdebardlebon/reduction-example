from functools import reduce
import math

print(reduce(lambda x, y: x+math.sqrt((y**5)//10), range(11)))
