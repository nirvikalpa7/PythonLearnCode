import time


# 202. Happy Number
# https://leetcode.com/problems/happy-number/

def is_happy(n: int) -> bool:
    if n == 1:
        return True
    data = {}
    print(n)
    while True:
        str_n = str(n)
        i = 0
        length = len(str_n)
        sum = 0
        while i < length:
            tmp = int(str_n[i])
            print("i=", i, ", tmp=", tmp)
            sum += tmp * tmp
            i += 1
            time.sleep(0.1)
        n = sum
        if n == 1:
            return True
        if data.get(n, 0) == 1:
            return False
        else:
            data[n] = 1
        print(data)


print(is_happy(19))
print("============================")
print(is_happy(2))
