import cv2
import os
import numpy as np


# 均值哈希算法
def aHash(img):
    pSize = 8
    # 缩放为8*8
    img = cv2.resize(img, (pSize, pSize))
    # 转换为灰度图
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    # s为像素和初值为0，hash_str为hash值初值为''
    s = 0
    hash_str = ''
    # 遍历累加求像素和
    for i in range(pSize):
        for j in range(pSize):
            s = s + gray[i, j]
    # 求平均灰度
    avg = s / (pSize * pSize)
    # 灰度大于平均值为1相反为0生成图片的hash值
    for i in range(pSize):
        for j in range(pSize):
            if gray[i, j] > avg:
                hash_str = hash_str + '1'
            else:
                hash_str = hash_str + '0'
    return hash_str


# Hash值对比
def cmpHash(hash1, hash2):
    n = 0
    # hash长度不同则返回-1代表传参出错
    if len(hash1)!=len(hash2):
        return -1
    # 遍历判断
    for i in range(len(hash1)):
        # 不相等则n计数+1，n最终为相似度
        if hash1[i] != hash2[i]:
            n = n + 1
    return n


def picCompare(pSample, pCapture):
    p3 = os.path.join(os.getcwd(), pSample)
    p4 = os.path.join(os.getcwd(), pCapture)

    print(p3)
    print(p4)

    img1 = cv2.imread(p3)
    img2 = cv2.imread(p4)

    hash1 = aHash(img1)
    hash2 = aHash(img2)

    n = cmpHash(hash1, hash2)

    return n


def dummpy_test(v1, v2):
    return v1 + v2


if __name__ == '__main__':
    n = picCompare("capture.png", "sample.png")
    print(n)
    # p1 = os.getcwd()
    # # p2 = os.path.pardir(p1)
    # p2 = os.path.dirname(p1)
    # p3 = os.path.join(p2, "sample.png")
    # p4 = os.path.join(p2, "WechatIMG706.png")
    #
    # img1 = cv2.imread(p3)
    # s1 = aHash(img1)
    #
    # img2 = cv2.imread(p4)
    # s2 = aHash(img2)
    # print(s1)
    # print(s2)
    #
    # n = cmpHash(s1, s1)
    # print(n)