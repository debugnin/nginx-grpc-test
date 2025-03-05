import grpc
import time
import service_pb2
import service_pb2_grpc

def run():
    # Create a gRPC channel
    channel = grpc.insecure_channel("nginx:8080")
    stub = service_pb2_grpc.GreeterStub(channel)

    while True:
        try:
            # Attempt to make a request
            response = stub.SayHello(service_pb2.HelloRequest(name="Frank"))
            print(f"Received from server: {response.message}")
            time.sleep(5)  # Send request every 5 seconds
        except grpc.RpcError as e:
            # Handle connection error and retry
            print(f"Connection error: {e}. Retrying...")
            time.sleep(2)  # Wait before retrying

if __name__ == "__main__":
    run()
