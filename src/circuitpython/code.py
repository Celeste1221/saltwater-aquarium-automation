# This code sets up a simple web server on a microcontroller that allows you to control actuators (like pumps and lights) via HTTP requests. 
# It connects to a Wi-Fi network, listens for incoming requests, and responds with the status of the actuators or toggles their state based on the request.
import wifi, socketpool, digitalio, board, json

# Connect to Wi-Fi
wifi.radio.connect("Your_SSID", "Your_PASSWORD")
pool = socketpool.SocketPool(wifi.radio)
print("Connected to", wifi.radio.ipv4_address)

# Define actuators
actuators = {
    "pump1": digitalio.DigitalInOut(board.D5),
    "light": digitalio.DigitalInOut(board.D6),
}

# Initialize actuators
for pin in actuators.values():
    pin.direction = digitalio.Direction.OUTPUT
    pin.value = False
    
# Set up the server socket
server_socket = pool.socket()
server_socket.bind((wifi.radio.ipv4_address, 80))
server_socket.listen(1)

# Define functions for handling actuator control
def toggle_actuator(name, state):
    if name in actuators:
        actuators[name].value = state
        return {"actuator": name, "state": state}
    return {"error": f"{name} not found"}

# Define function to get the status of all actuators
def get_status():
    return {k: v.value for k, v in actuators.items()}

# Start the server loop
while True:
    conn, addr = server_socket.accept()
    request = conn.recv(1024).decode()
    print("Request from", addr)

    if "GET /status" in request:
        response_data = get_status()
    elif "POST" in request and "/actuators/" in request:
        parts = request.split(" ")[1].split("/")
        if len(parts) == 4:
            _, _, actuator, action = parts
            response_data = toggle_actuator(actuator, action == "on")
        else:
            response_data = {"error": "Invalid endpoint"}
    else:
        response_data = {"error": "Unsupported request"}

    json_data = json.dumps(response_data)
    response = (
        "HTTP/1.1 200 OK\r\n"
        "Content-Type: application/json\r\n"
        f"Content-Length: {len(json_data)}\r\n"
        "Connection: close\r\n\r\n"
        f"{json_data}"
    )
    conn.send(response.encode())
    conn.close()
