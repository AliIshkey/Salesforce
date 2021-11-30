# Sample Application to integrate with salesforce

# To create a new 'Contact' in Salesforce:
sf.Contact.create({‘LastName’:Your surname’’, ‘Email’:’example@gmail.com’})

# To get a dictionary with all the information regarding that record, use:
sf.Contact.get_by_custom_id('My_Custom_ID__c', '22')

# To change that contact's last name and add a first name use:
sf.Contact.update('access token here',{'LastName': 'Your surname', 'FirstName': 'Your name'})

# To delete the contact:
sf.Contact.delete('access token here')

It's also possible to write select queries in Salesforce Object Query Language (SOQL) and search
queries in Salesforce Object Search Language (SOSL).


SOSL queries are done via

# To retrieve basic metadata use:
sf.Contact.metadata()

# To retrieve a description of the object, use:
sf.Contact.describe()

These are the related queries to perform operations on object into the salesforce
This is now a functioning API using Django Rest framework Request and Response objects.
This API also is able to handle different format suffixes and have explored how to POST data via the API.

