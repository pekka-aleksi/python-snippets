import asyncio
import time


async def action_1():
    for i in range(5):
        time.sleep(0.2)
        print(i, "action 1")

    print('action_1 done!')


async def action_2():
    for i in range(5):
        time.sleep(0.2)
        print(i, "action 2")

    print('action_2 done!')
    loop.stop()


start_time = time.perf_counter()

loop = asyncio.get_event_loop()

loop.create_task(action_1())
loop.create_task(action_2())

loop.run_forever()

print(f"Done in {time.perf_counter() - start_time:.3f}")
