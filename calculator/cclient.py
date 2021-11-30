import grpc

# import the generated classes
import calculator_pb2
import calculator_pb2_grpc

# open a gRPC channel
channel = grpc.insecure_channel('localhost:50051')

# create a stub (client)
stub = calculator_pb2_grpc.CalculatorStub(channel)


# make the call
while True:
    # create a valid request message
    # input = input()
    # val = int(input)
    number = calculator_pb2.Number(value=16)
    response = stub.SquareRoot(number)
    # et voilà
    print(response.value)
