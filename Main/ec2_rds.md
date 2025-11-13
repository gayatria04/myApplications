How to create AWS RDS Instance and Connect from MySQL Workbench
ChatGPT

### RDS and S3

1️⃣ Log in and Set Region
•	Log in to your AWS Management Console.
•	On the top-right corner, select Region: us-east-1 (N. Virginia).
________________________________________
2️⃣ Create RDS MySQL Instance
Go to: AWS Console → RDS → Databases → Create database
➤ Database creation method:
•	Choose Standard create
➤ Engine options:
•	Engine type: MySQL
•	Version: (Latest MySQL 8.x preferred)
➤ Templates:
•	Select Free Tier
➤ Settings:
•	DB instance identifier: mysql-lab-01
•	Master username: admin
•	Master password: Choose a secure password → Save it locally
➤ Instance configuration:
•	DB instance class: db.t3.micro ✅ (Free Tier)
➤ Storage:
•	Storage type: General Purpose (SSD)
•	Allocated storage: 20 GB
•	Disable storage autoscaling ❌
➤ Availability & durability:
•	Uncheck Multi-AZ deployment (not Free Tier)
➤ Connectivity:
•	VPC: Default
•	Public access: ✅ Enable temporarily
•	VPC security group: Create a new one named mysql-lab-sg
•	Inbound rules: Add rule for MySQL/Aurora (port 3306), source = Your IP only
➤ Additional configuration:
•	Initial database name: classicmodels
•	Backup retention: Set to 0 days
•	Enable deletion protection: ❌ Disable it (you’ll delete later)
➤ Tags:
Add:
name = mysql-lab-01
project = mysql-lab-01
roll_no = <your_roll_no>
date = <today’s_date>
✅ Click “Create database”
________________________________________
3️⃣ Wait for Instance to be “Available”
•	This takes 5–10 minutes.
•	Once ready, note:
o	Endpoint (hostname) (example: mysql-lab-01.xxx.us-east-1.rds.amazonaws.com)
o	Port: 3306
________________________________________
4️⃣ Connect via MySQL Workbench
1.	Open MySQL Workbench → “+” to add new connection.
2.	Connection settings:
o	Hostname: (RDS Endpoint)
o	Port: 3306
o	Username: admin
o	Password: (your password)
3.	Test Connection → If successful → Save → Connect.
If connection fails:
•	Ensure inbound rule in security group allows your current IP.
•	Public access must be enabled in RDS instance.
________________________________________
5️⃣ Import classicmodels.sql
1.	Download the classicmodels.sql dataset (from MySQL sample DB or your course folder).
2.	In Workbench:
o	Open File → Open SQL Script → select classicmodels.sql.
o	Choose the classicmodels database.
o	Click Execute All (⚡ icon).
✅ This imports all tables and data.
________________________________________
6️⃣ Export Database
After import completes:
1.	In Workbench → Server → Data Export
2.	Select schema: classicmodels
3.	Choose Export to Self-Contained File
o	Filename: classicmodels_export_01.sql
4.	Click Start Export
✅ This creates the export file on your computer.
________________________________________
# 7️⃣ Create S3 Bucket
Go to: AWS Console → S3 → Create bucket
•	Bucket name: rollno-bucket-01 (replace with your roll no)
•	Region: us-east-1
•	Block Public Access: Keep all checked ✅
•	Versioning: Disabled
•	Encryption: Default
➤ Tags:
name = rollno-bucket-01
roll_no = <your_roll_no>
project = mysql-lab-01
date = <today’s_date>
teacher_name = <teacher_name>
✅ Create bucket
________________________________________
8️⃣ Upload the Export File
1.	Inside your bucket → Click Upload
2.	Add file: classicmodels_export_01.sql
3.	Click Upload
✅ You can now download it anytime or verify by clicking the file → “Download”.
________________________________________
9️⃣ Verify and Cleanup
After confirming everything:
✅ Verify:
•	The SQL export file exists in S3.
•	You can download and open it.
🧹 Cleanup (very important to avoid charges):
1.	Delete RDS instance
o	RDS → Databases → select mysql-lab-01 → Actions → Delete
o	Uncheck “Create final snapshot”
o	Confirm deletion
2.	Delete S3 bucket
o	Empty the bucket → Delete bucket


### AWS EC2
1. Login with your Credentials.
2. Select EC2 from console home from dashboard.
3. From ec2 left side bar - dropdown -> Instances-> select Instances
4. Click on Launch instances from the center btn of the screen to build an instance.
5. Give it name and beside the name we have add additional tags btn, so add tags from there
6. Select application and os image 
7. Select Machine image that is as per the Configuration required- (ubuntu 22.04 LTS)
8. Select instance type that is Configuration of the system - (t2.micro)
9. Key pair login, which is used to connect to this instance from ssh using terminal-     a. Click on create a new key pair (we have to use our rollnos),   b. Keep pair type as RSA,  c. Private key file format as .pem
10. Network settings-  (there allow ssh is already enabled)- click on MyIp for access
11. Configure Storage -(You’ll see one existing volume):

Root volume (/dev/xvda) → change Size to 10 GiB, Then click Add New Volume → fill:

Size → 8 GiB

Volume type → gp3 (SSD)
12. Click on launch instance btn
13. View all instances- Click on the 
created.instance and we can see it as running
14. From the same page Click on connect to connect this to our browser
15.Connect to the Instance (SSH Login)

Select your instance → click Connect → choose SSH client tab.

Copy the SSH command (something like):

ssh -i "22IT123.pem" ubuntu@ec2-xx-xxx-xx-xx.compute-1.amazonaws.com


Open PowerShell (Windows) or Terminal (Mac/Linux).

Navigate to folder where .pem file is saved.

Paste the command and press Enter.

Type yes when prompted.
16. Once logged in, you’ll see:

ubuntu@ip-172-31-xx-xx:~$
17. Inside the terminal, run:

lsblk
18. Expected output:

NAME    MAJ:MIN RM  SIZE RO TYPE MOUNTPOINT
xvda    202:0    0   10G  0 disk
└─xvda1 202:1    0   10G  0 part /
xvdf    202:80   0    8G  0 disk



Video notes

1.	Open AWS Management console.
2.	click on RDS.
3.	Click on create database.
•	standard create by default chosen, let it be
•	Engine options – select MySQL
•	Choose 8.0.20 version
4.	Template – free tier
5.	In settings:-
•	DB instance identifier – give any name (name mentioned in question)
•	master username – leave it as admin
•	give any password of your wish
6.	Instance configuration – leave everything as it is
7.	Storage – disable storage autoscaling (mentioned in the question)
8.	(Video) Connectivity – Check public access as Yes (Imp)
•	in VPC security group – select default
•	rest leave as it is
(ChatGPT) ➤ Connectivity:
•	VPC: Default
•	Public access: ✅ Enable temporarily
•	VPC security group: Create a new one named mysql-lab-sg
•	Inbound rules: Add rule for MySQL/Aurora (port 3306), source = Your IP only
➤ Additional configuration:
•	Initial database name: classicmodels
•	Backup retention: Set to 0 days
•	Enable deletion protection: ❌ Disable it (you’ll delete later)
➤ Tags:
Add:
name = mysql-lab-01
project = mysql-lab-01
roll_no = <your_roll_no>
date = <today’s_date>

9.	Database authentication – leave it as it is
10.	rest everything leave as it is
11.	click on create database
12.	wait for some time and you’ll see the created database – when status is still in creating state, wait for some time – status should be (Available in green color)
13.	click on created database – copy the endpoint
14.	go to mysql workbench – click on the plus (+) icon in front of MySQL Connections
•	Setup new connection window will open
•	Connection name – give any name
•	Hostname – paste the endpoint
•	Username – whatever given while setting up RDS – in our case it is admin
•	in password – give the password you have given while creating RDS instance – click ok
•	default schema – leave it as it is
•	Click on test connection
15.	if you’re not able to connect to the instance or connection is getting timed out
•	open AWS RDS console – click on VPC security groups in security
•	go to inbound rules – click on edit inbound rules
•	click on add rule – select all traffic, select source – anywhere – Ipv4 – click on save rules
•	go back to SQL workbench – and click on test connection again
•	you should see – Successfully made the MySQL connection window – click ok – again click ok
16.	open RDS instance in workbench – now you can start writing your queries
17.	try creating database, use it and create table to test
18.	if table created successfully, your RDS connection is successful
Amazon AWS S3 (Simple Storage Service)
-	S3 – inexpensive object (think “file”) storage in AWS
-	Unlimited storage capacity, bcz of huge infrastructure size of amazon and it’s ability to scale.
-	Organized in “buckets” – top level containers to store videos, profile picture etc.
-	S3 is a flat file structure
-	Advantages - 1. Easy to Scale, 2. Accessible from anywhere, 3. inexpensive
1.	Go to Amazon S3 
2.	Click on create bucket
3.	Name it anything acc to you
4.	Choose region acc to you or mentioned in the question.
5.	In block public access settings, it has blocked all public access, leave it that way
6.	bucket versioning, let it be disabled – it is used to store multiple versions of objects or files in the bucket., but we don’t need it for our exam purpose (just like git, github)
7.	tags – helps you manage and organize things and to track your costs – click on add tag – give key value acc to you (in video – key – environment, value - dev)
8.	Default encryption – no change, leave it disabled
9.	Advanced settings – leave it as it is
10.	click on create bucket
11.	It should be visible on dashboard.
12.	click on it.
13.	Click on create folder – name it acc to you, keep rest of the things same – click on create folder.
14.	Click on videos folder – click upload – now you can select any picture or video from your PC and drag drop that here, and it will be uploaded, if you want to, you can configure properties below, but not necessary, you can leave it default and click on upload
15.	you can also upload it using AWS command line interface or programmatically using the software developer kit.
16.	It will show status succeeded 100%.
17.	Click on the file – click on open in the top right corner -  through object url you can access the file uploaded, but it will show access denied, bcz we have denied public access.
18.	to delete a bucket – go to amazon S3 – select the bucket you want to delete – click on delete available above it on right side – click on empty bucket configuration link – type – permanently delete – click empty – now click on delete bucket configuration visible on top with green message – enter the name of the bucket – click delete bucket – DONE


