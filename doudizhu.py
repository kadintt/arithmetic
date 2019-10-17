#!/usr/bin/env python3
# -*- coding: utf-8 -*-


import random


poker_num = [str(i) for i in range(2, 11)]
poker_str = ['J', 'Q', 'K', 'A']
poker_king = ['大王', '小王']
poker_color = ['红桃', '黑桃', '方块', '梅花']
pokers = ['%s%s' % (i, j) for i in poker_color for j in poker_num+poker_str]+poker_king

print(pokers)


random.shuffle(pokers)
# print(pokers)



print(len(pokers))

person_a = pokers[:-3:3]
person_b = pokers[1:-3:3]
person_c = pokers[2:-3:3]
landowner = pokers[-3:]
print(sorted(person_a))
print(sorted(person_b))
print(sorted(person_c))
print(len(person_a), len(person_b), len(person_c))
print(landowner)



cheng = lambda x, y: x**y


print(cheng(2, 3))