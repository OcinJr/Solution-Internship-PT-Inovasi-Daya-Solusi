
## **How to Run the Solution in Docker**
This solution is containerized using Docker environment.

Prerequisites:<br />
- Docker must be installed and running on your system.<br \>

Steps:<br />
1. Navigate to the Project Directory:<br />
   Open your terminal and change your directory to the root of this project (the folder containing the Dockerfile).<br \>

2. Build the Docker Image:<br />
Run the following command to build the Docker image.<br />
```docker build -t <fill with container name> .```<br />
- The -t flag tags the image with a memorable name.<br />
- The . at the end specifies the current directory as the build context.<br \>

3. Run the Docker Container:<br />
Once the image is successfully built, run the container using the command below.<br />
```docker run --rm <fill with container name>```<br \>

4. Expected Output<br />
After running the container, you will see the final merged data table and the transaction analysis printed directly to your console. <br \>

## **Summary**
From the historical table of c1:<br />
   - There are 5 transactions:<br />
      1. at 1.577956e+12  the balance is changed from 0 to 15000.0<br />
      2. at 1.578314e+12  the credit used 12000.0<br />
      3. at 1.578420e+12  the credit used 19000.0<br />
      4. at 1.578649e+12  the balance is changed 15000.0 to 40000.0<br />
      5. at 1.578654e+12  the balance is changed 40000.0 to 21000.0<br />


From the historical table of c2:<br />
   - There are 2 transactions:<br />
      1. at 1.579361e+12  the credit used 37000.0<br />
      2. at 1.578649e+12  the balance is changed 21000.0 to 33000.0<br />

## **Thinking Behind the Solution**
**Data Merging and Consolidation**<br \>
To create a complete historical timeline, it was crucial to combine all records from all source tables without losing any data. An outer join (pd.merge(..., how="outer")) was chosen for this reason. This type of join keeps every record from both tables, creating NaN values where data doesn't exist in one of the sources for a given key. This ensures that every single timestamped event is included in the final dataset.<br \>

**Handling Missing Data**<br \>
The outer join naturally results in records with missing information. Since information like account_id, name, and card_number is persistent, a forward fill (ffill()) was used. This method propagates the last valid observation forward, correctly filling in the user details for all subsequent events until a new change is recorded.<br \>