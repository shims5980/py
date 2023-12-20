import asyncio
import random

async def show():
    x=random.sample([1,2,3,4,5,6], k=1)
    await asyncio.sleep(x[0])       # x가 리스트 형태로 반환되어 옴
    print(x)

async def main():
    await asyncio.gather(
        show(),
        show(),
        show(),
        show(),
        show(),
        show()
    )
asyncio.run(main())