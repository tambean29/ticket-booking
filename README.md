Project Overview:
django web-applicaton ticket-booking; allows users to book available shows and remove them from the history; allow admins to add shows and remove shows; view history.

Setup and run instructions:
1. clone the repository 
git clone https://github.com/tambean29/ticket-booking
2. run in terminal
docker-compose build
docker-compose up
3. The app should be available on http://localhost:8000

Tech stack used:
containerization - docker
CI/CD - Jenkins
Database - MysSQL 8.0

Usage Notes:
Docker:
1. to stop the docker containers run the following command in terminal:
docker-compose down
2. to delete the containers along with the database in the docker:
docker-compose down -v

Project demo video:
![project demo](./assets/ticket-booking-demo.gif)

Jenkins:
Used to automate build,test and deploy.
Required plugin: Docker Pipeline 
To install Docker Pipeline Plugin:
1. go to localhost:8080 > manage jenkins > Plugins > Available plugins.
2. Search Docker Pipeline and install  it 

To run the project using Jenkins:
1. click new item
2. give a name to the item and select pipeline as item type and click ok.
3. Under Pipeline select " Pipeline script from SCM"
4. Under SCM select "Git"
5. In the Repository URL field provide "https://github.com/tambean29/ticket-booking"
6. Under branch to build field provide "*/main"
7. Under Script Path field provide "Jenkinsfile"
