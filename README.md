# my-flexlogger-project
 This example illustrates how you can use DIAdem 2020 with SystemLink 2020 R3 and higher to automatically trigger PDF reports to be generated when new TDMS files arrive from a product like FlexLogger 2020 R3, but it could be easily modified to trigger reports on any file sent from any application (i.e. LabVIEW).
 
 # Instructions
 1. Load the TDR file in DIAdem and customize the report to match the channels in your files
 2. Open the ANP file in DIAdem and replace the TDR file with your new one and modify the query conditions to match your TDMS file.
 3. Save the ANP file and then using the SystemLink Analysis Automation application add it to the Analysis Automation Procedures Library.
 4. Create a Triggered Task under you Analysis Automation instance and specify the data source as the FileIndex and specify your new analysis prodedure.
 5. Make sure you Apply your changes
 6. Ensure FlexLogger is configured to enable publishing files and tags to SystemLink.
 7. Run your FlexLogger application or upload a new file to the SystemLink File Ingestion service using one if its suppported APIs (LabVIEW, C#, Python, TestStand) or via the SystemLink File Viewer web interface.
