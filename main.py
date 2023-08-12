import asyncio
from typing import Tuple


class App:
    def __init__(self) -> None:
        self.name = "async testing"

    async def start(self) -> None:
        print('starting...')
        await self.main_loop()

    async def main_loop(self) -> None:
        count: int = 1
        tasks: list[Tuple[asyncio.Task, int]] = []
        while True:
            try:
                if len(tasks) < 5:
                    task = asyncio.create_task(self.foo(count))
                    print(type(task))
                    tasks.append((task, count))
                    print(f'task {count} appended')
                    count += 1
            except Exception as e:
                print(f'There was an unexpected error: {e}')
            finally:
                while tasks and tasks[0][0].done():
                    print(f'Task {tasks[0][1]} complete')
                    tasks.pop(0)
                await asyncio.sleep(0.1)

    async def foo(self, count: int) -> None:
        print(f'Task {count} starting')
        await asyncio.sleep(5)  # sleep for 5 seconds
        print(f'Task {count} ending')


async def main() -> None:
    app = App()
    await app.start()


if __name__ == '__main__':
    asyncio.run(main())
