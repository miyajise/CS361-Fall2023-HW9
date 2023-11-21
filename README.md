#CS361 Assignment 9 
by Sharyn Miyaji

Partner: James Hill


**How to programmatically REQUEST data:**

In the bankcomms.txt file, the first line must contain the word "request" in order to start the microservice.  After
the first line, the name of the player, the action ('deposit'/'receive'), and the amount must be written using a space to
separate the variables.  Below is an example of what the bankcomms.txt file should be formatted for the microservice to 
work successfully, where John is the name of the player, 'deposit' is the action and 1000 is the amount to be deposited to John's bank account.

![](sample_request.png)

**How to programmatically RECEIVE data:**

Once the request is completed, the bankcomms.txt file will have the phrase "Successfully received" to indicate that the
transaction is completed for the player.  

**UML Diagram:**

![](UML_diagram.png)
