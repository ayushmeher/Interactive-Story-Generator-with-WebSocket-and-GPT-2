import asyncio
from rich.console import Console
from story_generator import StoryGenerator

console = Console()

async def main():
    # Initialize story generator
    generator = StoryGenerator()

    # Start story generation
    await generator.start_story()

    # Wait for user input
    while True:
        user_input = console.input("[bold magenta]Enter your choice: [/bold magenta]")
        await generator.process_user_input(user_input)

if __name__ == '__main__':
    try:
        asyncio.run(main())
    except KeyboardInterrupt:
        print("\n[bold red]Disconnected from the server.[/bold red]")
