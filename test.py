# import os
# import sys
# def main():
#     bag = {}
#     with open('C:\\Users\\Administrator\\Desktop\\database\\Test language\\New folder\\dataset\\conversation data\\test2.txt','r',encoding = 'utf8') as fp:
#         cnt = 0
#         for line in fp:
#             print('line {} contents {}'.format(cnt,line))
#             record_word_cnt(line.strip().split(' '),bag)
#             cnt += 1
#     sorted_words = order_bag(bag,desc=True)
#     print("Most frequent 10 words {}".format(sorted_words[:20]))

# def order_bag(bag,desc=False):
#     words = [(word, cnt) for word, cnt in bag.items()]
#     return sorted(words, key=lambda x: x[1], reverse=desc)

# def record_word_cnt(words,bag):
#     for word in words:
#         if word != '':
#             if word.lower() in bag:
#                 bag[word.lower()] += 1
#             else:
#                 bag[word.lower()] = 1
# if __name__ == '__main__':
#     main()
# phần mềm đếm từ ở trên

def fib(n):    # write Fibonacci series up to n
    """Print a Fibonacci series up to n."""
    result = []
    a, b = 0, 1
    while a < n:
        result.append(a)
        # print(a, end=' ')
        a, b = b, a+b
        # print()
    return result
f100 = fib(1000)
print(f100)