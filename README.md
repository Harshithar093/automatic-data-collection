# automatic-data-collectionDesigning an Automatic Data Collection and Storage
System with AWS Lambda and Slack Integration for Server
Availability Monitoring and Slack Notification


1.Create the lambda function to fetch the data from API(http://api.open-notify.org/iss-now.json)
--> To fetch the data from the API, the function should use the requests library (or a similar
library) to make a GET request to the API.

2.Create a cloudwatch rule to schedule that lambda function
-->For example cron(0 12 * * ? *) runs the rule every day at 12:00pm UTC+0.
 (0/1 * * * ?*)
 
3.Create a Amazon RDS(postgresdb) to store the fetched API data
-->The function should then use a library such as
psycopg2 to connect to the Amazon RDS instance and store the data in the database

4.Create the Amazon CloudWatch to set up a monitoring alarm that will trigger when the
server is unavailable
--> Go to the insatnce and Copy the instance ID /resource ID and create metric filter
--> create alarm for the metric add teh threshold

5.Use the Slack API to send a message to your Slack community when the alarm is
triggered.
--> integrate with slack for notification when the alarm is triggered.

