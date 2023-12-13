#!/usr/bin/env python3
# -*- coding: utf-8 -*-

if __name__ == '__main__':
    n = 10

    for i in range(1, 100):
        n += n / 10
        if n > 15:
            print(i)
            break
