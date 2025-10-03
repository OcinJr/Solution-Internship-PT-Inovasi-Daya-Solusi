
## **How to Run the Solution in Docker**
This solution is containerized using Docker environment.

Prerequisites:<br />
- Docker must be installed and running on your system.

Steps:<br />
1. Navigate to the Project Directory:<br />
   Open your terminal and change your directory to the root of this project (the folder containing the Dockerfile).

2. Build the Docker Image:<br />
Run the following command to build the Docker image.<br />
```docker build -t <fill with container name> .```<br />
- The -t flag tags the image with a memorable name.<br />
- The . at the end specifies the current directory as the build context.

3. Run the Docker Container:<br />
Once the image is successfully built, run the container using the command below.<br />
```docker run --rm <fill with container name>```

4. Expected Output<br />
After running the container, you will see the final merged data table and the transaction analysis printed directly to your console. 

## **Summary**
from the historical table of c1:<br />
   - there are 5 transactions:<br />
      1. at 1.577956e+12  the balance is changed from 0 to 15000.0<br />
      2. at 1.578314e+12  the credit used 12000.0<br />
      3. at 1.578420e+12  the credit used 19000.0<br />
      4. at 1.578649e+12  the balance is changed 15000.0 to 40000.0<br />
      5. at 1.578654e+12  the balance is changed 40000.0 to 21000.0<br />


from the historical table of c2:<br />
   - there are 2 transactions:<br />
      1. at 1.579361e+12  the credit used 37000.0<br />
      2. at 1.578649e+12  the balance is changed 21000.0 to 33000.0<br />