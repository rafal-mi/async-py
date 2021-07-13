import asyncio
import os

async def main():
    read, write = os.pipe()
    process_1 = await asyncio.create_subprocess_shell('./script-1.sh', stdout=write)
    os.close(write)
    process_2 = await asyncio.create_subprocess_shell('./script-2.sh', stdin=read, stdout=asyncio.subprocess.PIPE)
    os.close(read)
    return await process_2.stdout.read()

if __name__ == '__main__':
    output = asyncio.run(main())
    print(output.decode('utf-8'))

