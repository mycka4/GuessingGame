import socket

host = "localhost"
port = 7777


s = socket.socket()
s.connect((host, port))


data = s.recv(1024)
print(data.decode().strip())


while True:
    try:
        difficulty = int(input("Enter difficulty (1-easy, 2-medium, 3-hard): ").strip())
        if difficulty in [1, 2, 3]:
            break
        else:
            print("Invalid choice. Choose 1, 2, or 3.")
    except ValueError:
        print("Please enter a valid number.")


s.sendall(str(difficulty).encode())


if difficulty == 1:
    low, high = 1, 10
elif difficulty == 2:
    low, high = 1, 50
else:
    low, high = 1, 100


data = s.recv(1024)
print(data.decode().strip())


while True:
    guess = (low + high) // 2
    print(f"Bot guesses: {guess}")
    s.sendall(str(guess).encode())
    reply = s.recv(1024).decode().strip()
    print(f"Server reply: {reply}")

    if "CORRECT!" in reply:
        break
    elif "Lower" in reply:
        high = guess - 1
    elif "Higher" in reply:
        low = guess + 1

s.close()
