import time as t

class MyTimer():
    def __init__(self):
        self.unit = ['年','月','日','小时','分钟','秒']
        self.prompt = '未开始计时'
        self.lasted =[]
        self.begin = 0
        self.end = 0

    def __str__(self):
        return self.prompt

    __repr__ = __str__

    def __add__(self, other):
        prompt = 'the total running time is:'
        result = []
        for index in range(6):
            result.append(self.lasted[index] + other.lasted[index])
            if result[index]:
                prompt += (str(result[index])+self.unit[index])
        return prompt

    #start
    def start(self):
        self.begin = t.localtime()
        self.prompt = 'warning:please use stop() to stop!'
        print('start the time...')

    #stop
    def stop(self):
        if not self.begin:
            print('warning:please use start() to start!')
        else:
            self.end = t.localtime()
            self._calc()
            print('stop the time!')

    #inner method,calculate the running time
    def _calc(self):
        self.lasted = []
        self.prompt = 'the total running time is:'
        for index in range(6):
            self.lasted.append(self.end[index] - self.begin[index])
            if self.lasted[index]:
                self.prompt += (str(self.lasted[index]) + self.unit[index])
t1 = MyTimer()
print(t1)
t1.start()


t1.stop()
print(t1)