from bootstrap.wrappers import AsyncPrintWrapper, ReadStdinAndHashWrapper
from app.functions import getvactext, hashlines

import asyncio


class Task(object):
    async def run(self):
        apw = AsyncPrintWrapper(getvactext)
        await apw.run()
        rwr = ReadStdinAndHashWrapper(hashlines)
        rwr.run()


async def main():
    tt = Task()
    await tt.run()


if __name__ == '__main__':
    asyncio.run(main())
