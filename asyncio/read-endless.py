import asyncio
import os

async def main():
    process = await asyncio.create_subprocess_shell('./script-1.sh', stdout=asyncio.subprocess.PIPE)
   
    async for data in process.stdout:
        line = data.decode('ascii').rstrip()
        print(line)

if __name__ == '__main__':
    asyncio.run(main())

