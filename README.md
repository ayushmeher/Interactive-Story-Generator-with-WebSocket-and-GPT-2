
# Interactive Story Generator with WebSocket and GPT-2

This project is an **Interactive Story Generator** that allows users to participate in a dynamic storytelling experience powered by GPT-2. It uses WebSockets for real-time communication, enabling user choices to influence the direction of the story. The system narrates the story using `pyttsx3` for text-to-speech and leverages `torch` for deep learning inference with GPT-2.

## Project Structure

- **main.py**: Runs the main interactive session, initializes the story generator, and handles user input.
- **story_generator.py**: Manages story generation using GPT-2, processes user input via WebSocket, and generates responses.
- **web_socket_server.py**: Sets up a WebSocket server to manage user interactions, processing choices to drive the story forward.
- **utils.py**: Contains a text-to-speech function using `pyttsx3` for narrating story segments.
- **requirements.txt**: Lists the required libraries.

## Key Features

1. **GPT-2 Story Generation**: Uses the pre-trained GPT-2 model to generate story content, with user choices affecting the narrative flow.
2. **Real-Time Interaction**: WebSocket-based server allows real-time interaction and choice-driven storytelling.
3. **Narration**: Implements `pyttsx3` for narrating story segments to enhance the immersive experience.
4. **User-Driven Plot**: Responds to user choices to create a customized story experience.

## Requirements

- Python 3.x
- Libraries: Transformers, Rich, pyttsx3, WebSockets, torch

Install dependencies using:
```bash
pip install -r requirements.txt
```

## Usage

1. **Start the WebSocket Server**:
   Run the WebSocket server in `web_socket_server.py` to handle incoming user connections and responses.
   ```bash
   python web_socket_server.py
   ```

2. **Launch the Main Program**:
   Start the main interactive story session in `main.py`, where you can provide inputs to steer the story.
   ```bash
   python main.py
   ```

3. **Interact with the Story**:
   - The program will prompt you to make choices as the story progresses.
   - Enter "A" or "B" to choose different paths, and the system will generate the next story segment based on your choice.

## Example

- Initial story prompt: “In a distant land, there was a mystical forest where strange creatures roamed freely...”
- User selects option "A" or "B".
- The program responds with a new story segment based on the chosen option, narrates it, and displays the text in the console.

## File Details

- **main.py**: Handles the main program flow, initializes the story generator, and waits for user inputs.
- **story_generator.py**: Loads GPT-2, generates story text, manages WebSocket connection, and processes user choices.
- **web_socket_server.py**: Hosts the WebSocket server, processes user options, and sends responses back to `story_generator.py`.
- **utils.py**: Defines a `narrate_text` function that uses `pyttsx3` to convert story text to speech.

## Contributing

Contributions are welcome to expand the choice options, enhance story generation prompts, or improve real-time interaction.

## License

This project is open-source and available under the MIT License.
