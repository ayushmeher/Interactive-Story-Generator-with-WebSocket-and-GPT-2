import asyncio
import torch
from transformers import GPT2Tokenizer, GPT2LMHeadModel
from rich import print
from rich.console import Console
from utils import narrate_text
import websockets

console = Console()

class StoryGenerator:
    def __init__(self):
        # Initialize GPT-2 model and tokenizer
        self.tokenizer = GPT2Tokenizer.from_pretrained('gpt2')
        self.model = GPT2LMHeadModel.from_pretrained('gpt2')

        # Move model to GPU if available
        device = torch.device('cuda' if torch.cuda.is_available() else 'cpu')
        self.model.to(device)

        # Initialize WebSocket connection
        self.websocket = None

    async def start_story(self):
        # Generate initial story
        story = self.generate_story()

        # Narrate initial story
        narrate_text(story)

        # Print initial story
        console.print(f"[bold blue]{story}[/bold blue]")

        # Establish WebSocket connection
        async with websockets.connect("ws://localhost:8765") as websocket:
            self.websocket = websocket

    async def process_user_input(self, user_input):
        # Send user input to WebSocket server
        await self.websocket.send(user_input)

        # Receive response from WebSocket server
        response = await self.websocket.recv()

        # Generate next part of story
        next_story = self.generate_next_story(response)

        # Narrate next part of story
        narrate_text(next_story)

        # Print next part of story
        console.print(f"[bold blue]{next_story}[/bold blue]")

    def generate_story(self):
    # Provide a more complex initial story prompt
        input_text = "In a distant land, there was a mystical forest where strange creatures roamed freely. The air was thick with magic, and adventurers often got lost in its depths."
        input_ids = self.tokenizer.encode(input_text, return_tensors='pt')
        output = self.model.generate(input_ids, max_length=100)
        return self.tokenizer.decode(output[0], skip_special_tokens=True)

    def generate_next_story(self, prompt):
        # Generate next part of story using GPT-2
        input_ids = self.tokenizer.encode(prompt, return_tensors='pt')
        output = self.model.generate(input_ids, max_length=100)
        return self.tokenizer.decode(output[0], skip_special_tokens=True)