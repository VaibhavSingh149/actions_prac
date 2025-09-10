import os 
def connect_to_service():
    api_key = os.getenv("API_KEY", "default_key")
    print(f"Connecting to the server with {api_key}")

if __name__ == "__main__":
    print("Starting application...")
    connect_to_service()
    print("Application closed")

    