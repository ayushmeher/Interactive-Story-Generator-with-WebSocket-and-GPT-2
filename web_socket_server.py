import asyncio
import websockets

async def handle_connection(websocket, path):
    while True:
        try:
            # Receive user input from client
            user_input = await websocket.recv()
            print(f"Received: {user_input}")

            # Respond with a twist (dummy response for now)
            if user_input == "A":
                response = "You chose option A. Here's the next part of the story..."
            elif user_input == "B":
                response = "You chose option B. Here's the next part of the story..."
            else:
                response = "Invalid choice. Please choose again."

            # Send response back to client
            await websocket.send(response)
        except websockets.ConnectionClosed:
            print("Client disconnected")
            break

async def main():
    async with websockets.serve(handle_connection, "localhost", 8765):
        await asyncio.Future()  # run forever

if __name__ == '__main__':
    print("Starting WebSocket server...")
    asyncio.run(main())
