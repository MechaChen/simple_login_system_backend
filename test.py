import sys
import subprocess

print("Testing Python version...")
print(sys.version)

print("Testing AWS CLI...")
try:
    subprocess.run(["aws", "--version"])
except FileNotFoundError:
    print("AWS CLI not found")

print("Testing Serverless Framework...")
try:
    subprocess.run(["serverless", "--version"])
except FileNotFoundError:
    print("Serverless Framework not found")

print("Testing npm version...")
try:
    subprocess.run(["npm", "-v"])
except FileNotFoundError:
    print("npm not found")

print("All tests completed!")
