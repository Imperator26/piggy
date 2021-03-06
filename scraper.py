import asyncio

from piggy.piggy import Piggy


async def main(pig):
    async for media in pig.feed():
        await pig.download(media)

# Loop
loop = asyncio.get_event_loop()

pig = Piggy()

try:
    loop.run_until_complete(pig.setup())
    loop.run_until_complete(pig.login())

    loop.run_until_complete(main(pig))

except KeyboardInterrupt:
    for task in asyncio.Task.all_tasks():
        task.cancel()
    pass

finally:
    loop.run_until_complete(pig.close())

loop.close()
