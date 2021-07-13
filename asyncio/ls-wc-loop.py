import asyncio
import os

async def one_run():
    read, write = os.pipe()
    process_1 = await asyncio.create_subprocess_exec('find', os.getenv("HOME"), stdout=write)
    os.close(write)
    process_2 = await asyncio.create_subprocess_exec('wc', '-l', stdin=read, stdout=asyncio.subprocess.PIPE)
    os.close(read)
    output = await process_2.stdout.read()
    print(output.decode('utf-8'))

async def main():
    for i in range(12):
        await one_run()


if __name__ == '__main__':
    asyncio.run(main())

