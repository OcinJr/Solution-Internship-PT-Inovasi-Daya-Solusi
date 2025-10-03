
## How to Run the Solution in Docker
This solution is containerized using Docker environment.

Prerequisites:
- Docker must be installed and running on your system.

Steps:
1. Navigate to the Project Directory:
   Open your terminal and change your directory to the root of this project (the folder containing the Dockerfile).

2. Build the Docker Image:
   Run the following command to build the Docker image.
   "docker build -t <fill with container name> ."
   - The -t flag tags the image with a memorable name.
   - The . at the end specifies the current directory as the build context.

3. Run the Docker Container:
Once the image is successfully built, run the container using the command below. 
"docker run --rm <fill with container name>"

4. Expected Output
After running the container, you will see the final merged data table and the transaction analysis printed directly to your console. 

## Summary
from the historical table of c1:
   there are 5 transactions:
      at 1.577956e+12  the balance is changed from 0 to 15000.0
      at 1.578314e+12  the credit used 12000.0
      at 1.578420e+12  the credit used 19000.0
      at 1.578649e+12  the balance is changed 15000.0 to 40000.0
      at 1.578654e+12  the balance is changed 40000.0 to 21000.0


from the historical table of c2:
   there are 2 transactions:
      at 1.579361e+12  the credit used 37000.0
      at 1.578649e+12  the balance is changed 21000.0 to 33000.0