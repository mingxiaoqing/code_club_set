"""
哈希算法解析查找问题
"""

from collections import defaultdict


def parse(target):
    """双指针查找方法"""
    res = []
    try:
        lst1 = lst[:]
        lst1.sort()
        left = 0
        right = len(lst1) - 1
        while left < right:
            if lst1[left] + lst1[right] < target:
                left += 1
            elif lst1[left] + lst1[right] > target:
                right -= 1
            else:
                for item in range(len(lst)):
                    if lst[item] == lst1[left]:
                        res.append(item)
                        break
                    for i in range(len(lst)-1, -1, -1):
                        if lst[i] == lst1[right]:
                            res.append(right)
                            break
                res.sort()
                break
    except Exception as err:
        print(err)
    return res


def hash_two_sum(target):
    """哈希查找方法"""
    dic = dict()
    for i in range(len(lst)):
        num = lst[i]
        if target - num in dic:
            return dic[target - num] + 1, i + 1
        dic[num] = i


def word_pattern(word_pat):
    word = input().split()
    if len(word) != len(word_pat):
        return False
    hashs = {}
    used = {}
    for i in range(len(word_pat)):
        print()
        if word_pat[i] in hashs:
            if hashs[word_pat[i]] != word[i]:  # 不是第一次出现 检查映射关系是否一致
                return False
        else:
            if word[i] in used:
                return False
            hashs[word_pat[i]] = word[i]
            used[word[i]] = True
    return True


def replace_word(words, sentence):
    d = defaultdict(set)
    s = defaultdict(int)
    sentence = sentence.split()
    for w in words:
        d[w[0]].add(w)
        s[w[0]] = max([s[w[0]], len(w)])
    for i, w in enumerate(sentence):
        for j in range(s[w[0]]):
            if w[:j+1] in d[w[0]]:
                sentence[i] = w[:j+1]
                break
    return " ".join(sentence)


def guess_word(secret, guess):
    secret_dic = {}
    guess_dic = {}
    A = 0
    B = 0
    for i in range(len(secret)):
        if secret[i] == guess[i]:
            A += 1
        else:
            if secret[i] not in secret_dic:
                secret_dic[secret[i]] = 1
            else:
                secret_dic[secret[i]] += 1
            if guess[i] not in guess_dic:
                guess_dic[guess[i]] = 1
            else:
                guess_dic[guess[i]] += 1
    for j in secret_dic:
        if j in guess_dic:
            B += min(secret_dic[j], guess_dic[j])
    return ''.join([str(A), 'A', str(B), 'B'])


if __name__ == '__main__':
    # 给一个有序列表, 查找和为n的数字下标
    lst = [3, 4, 5, 7, 10]
    n = 11
    # 双指针法
    arg = parse(n)
    print(arg)
    # 哈希算法
    print(hash_two_sum(n))

    # 查找单词映射关系
    print(word_pattern([1, 2, 2]))

    # 词根替换
    words = ['cat', 'rat', 'bat']
    sentence = "the cattle was rattled by the battery"
    print(replace_word(words, sentence))

    # 猜词游戏
    secret = '1123'
    guess = '9111'
    print(guess_word(secret, guess))
