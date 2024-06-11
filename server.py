import socket, threading

HOST = '0.0.0.0' 
PORT = 3434        

accounts = {
    "morhaf": 10050,
    "saleh": 7000,
    "almahde": 2000
}

def handle_client(conn, addr):
    print("Connected by {}".format(addr))
    while True:
        data = conn.recv(1024).decode()
        if not data:
            break

        account_number, operation, amount = data.split()
        if account_number not in accounts:
            conn.sendall("Invalid account Name".encode())
            continue

        try:
            amount = float(amount)
        except ValueError:
            conn.sendall("Invalid amount".encode())
            continue

        if operation == "check_balance":
            balance = accounts[account_number]
            conn.sendall("Your balance is: {}".format(balance).encode())
        elif operation == "deposit":
            accounts[account_number] += amount
            conn.sendall("Deposit successful. New balance: {}".format(accounts[account_number]).encode())
        elif operation == "withdraw":
            if accounts[account_number] < amount:
                conn.sendall("Insufficient funds".encode())
            else:
                accounts[account_number] -= amount
                conn.sendall("Withdrawal successful. New balance: {}".format(accounts[account_number]).encode())
        else:
            conn.sendall("Invalid operation".encode())

    conn.close()
    print("Client {} disconnected".format(addr))

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.bind((HOST, PORT))
    s.listen()
    print("Server listening on {}:{}".format(HOST, PORT))
    while True:
        conn, addr = s.accept()
        thread = threading.Thread(target=handle_client, args=(conn, addr))
        thread.start()
