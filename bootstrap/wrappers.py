import asyncio
import random
import sys


class AsyncPrintWrapper(object):

    def __init__(self, f):
        self.f = f

    async def run(self):
        task_list = []
        for _ in range(1, 5):
            task = asyncio.create_task(self._task())
            task_list.append(task)
        await asyncio.gather(*task_list)

    async def _task(self):
        t_sleep = random.randint(1, 5)
        await asyncio.sleep(t_sleep)
        print(self.f())


class ReadStdinAndHashWrapper(object):

    def __init__(self, f):
        self.f = f

    def run(self):
        print('Ввод до нажатия ^D(CTRL-D)')
        lines = sys.stdin.readlines()
        print(self.f(lines))


