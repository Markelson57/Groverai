import asyncio
from core import Core

async def main():
    core = Core()
    await core.event_loop()

if __name__ == "__main__":
    asyncio.run(main())
