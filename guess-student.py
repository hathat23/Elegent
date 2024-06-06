import time

length = 5
routine = 1
times = 200
password = "abcde"

# 模拟第三种登录过程
def login(input):
    for i in range(0, len(input)):
        if password[i] != input[i]:
            return False
        # 模拟延时
        time.sleep(0.00001)
    return True


# 获取密码验证耗费时间和验证次数
def getRunTimeAndVerificationTimes(input):
    t1 = time.time()
    verification_times = 0
    # 多次验证，累计时间
    for i in range(int(times)):
        verification_times += 1
        if login(input):
            t2 = time.time()
            runTime = t2 - t1
            return runTime, verification_times
    t2 = time.time()
    runTime = t2 - t1
    return runTime, verification_times


if __name__ == "__main__":
    for a in range(routine):
        result = ""
        for index in range(int(length)):
            # 验证次数随已猜测字符串长度增加而减少
            times /= (index + 1)
            # 补充：输出当前已猜测的字符串
            print("Current guess:", result)
            maxTime = 0
            bestLetter = ''
            for i in range(26):
                letter = chr(ord('a') + i)
                runTime, verification_times = getRunTimeAndVerificationTimes(result + letter)
                # 补充：输出运行时间
                print("Runtime for", result + letter + ":", runTime)
                # 补充：输出验证次数
                print("Verification times for", result + letter + ":", verification_times)
                if runTime > maxTime:
                    maxTime = runTime
                    bestLetter = letter
            result += bestLetter
            # 补充：输出此次比较的结果
            print("Best guess:", result)
            print(str(index / length * 100) + "%")
        print("100.0%")

        print("Final result:", result)
