<!-- # atlys
Atlys Assignment

I have created a folder scrapper_app which contain the FastAPI having the required scrapping application


1. The folder contain a docker-compose.yaml file which will help you build the application and run it in docker container
1.1 Make sure you are inside the scrapper_app folder and run the follwoing command
    - docker-compose up -d
1.2 Once the docker image gets build, it will run the docker container for the application in detched mode, once done, check the docker container is running or not
    - docker ps
1.3 Once you get the docker image id, check the logs
    - docker logs -f <docker-id>
1.4 Hit with the Healthcheck API, given below
1.5 Hit the scrapping API with proper payload, given below
1.6 To check the procedure of the scrapping and it got saved in the respective local environment or not exec inside the docker container
    - docker exec -it <docker-id> sh
    - ls
    - you will get list of folders in the root work directory
        - our interest is to check the images inside - downloaded_images
            - cd downloaded_images
            - ls
        - another interest of ours is to check the local storage of scrapped data in json file
            - go back to the root work directory, parent of downloaded_images
            - cat scraped_data.json

------- ANOTHER WAYS TO UP AND RUN THE APPLICTION -------

2. The folder contain a Dockerfile which you will use to build and run the application
2.1 Make sure to build the docker image for the application
    - You just need to enter inside the scrapper_app folder and run the following command
    - docker build -t app .
2.2 Once the image build gets completed then you need to run the image
    - docker run -p 8000:8000 app

3. If you don't want to run it using Docker then you can user uvicorn -
3.1 You just need to enter inside the scrapper_app folder and install all the dependencies
    - pip install -r requirements.txt
3.2 And then run the uvicorn command to start the application
    - uvicorn app.main:app --reload
3.3 If needed do set the environment -
    - python3 -m venv path/to/venv
    - source path/to/venv/bin/activate
    - pip install -r requirements.txt
    - uvicorn app.main:app --reload


4. There are 2 API's Supported:
4.1 Curl for health check is -
    - curl --location 'http://0.0.0.0:8000/'
4.2 Curl for scrapping is -
    - curl --location 'http://0.0.0.0:8000/scraper/start' \
        --header 'Authorization: Bearer 1234' \
        --header 'Content-Type: application/json' \
        --data '{
        "pages": 15,
        "url": "https://dentalstall.com/shop/"
        }'

The second curl will take pages as optional paramener and the Authorization header in headers.

# for current scenario i have set the following configuration and didn't put it in .env environment file to make the execution easy
STATIC_TOKEN = "1234"  
PROXY = None 
MAX_RETRIES = 3
RETRY_DELAY = 5

 -->
# Atlys Assignment

## Overview
This repository contains a FastAPI-based web scraper application located in the `scrapper_app` folder. The application supports scraping data from specified URLs and stores the results in a local environment.

## Setup Instructions

### Method 1: Using Docker (Preferred)
The project includes a `docker-compose.yaml` file to easily build and run the application within a Docker container.

#### Steps:
1. **Navigate to the `scrapper_app` folder**:
   ```bash
   cd scrapper_app
Build and run the application using Docker:

bash
Copy code
docker-compose up -d
This will build the Docker image and run the container in detached mode.

Verify the running container: Check if the Docker container is running:

bash
Copy code
docker ps
Check the logs of the running container: Get the container ID and view the logs:

bash
Copy code
docker logs -f <docker-id>
Access the Health Check API: Verify the health of the application by hitting the Health Check API.

Trigger the Scraping API: Call the scraping API with the appropriate payload (see the Scraping API section below).

Verify Scraping Results: To ensure that the scraping process worked, you can access the container and check the stored data:

bash
Copy code
docker exec -it <docker-id> sh
Inside the container:

List folders:
bash
Copy code
ls
Navigate to the downloaded_images folder and verify image files:
bash
Copy code
cd downloaded_images
ls
Check the scraped data in the scraped_data.json file:
bash
Copy code
cd ..
cat scraped_data.json
Method 2: Using Dockerfile
If you prefer to use the Dockerfile to build and run the application manually, follow these steps:

Build the Docker image: Inside the scrapper_app folder, run:

bash
Copy code
docker build -t app .
Run the application container: After the image is built, run it using the following command:

bash
Copy code
docker run -p 8000:8000 app
Method 3: Running Locally with Uvicorn
If you prefer to run the application locally without Docker, you can use Uvicorn.

Install dependencies: Inside the scrapper_app folder, install the required Python dependencies:

bash
Copy code
pip install -r requirements.txt
Start the application with Uvicorn:

bash
Copy code
uvicorn app.main:app --reload
Optional: Set up a virtual environment: If you wish to use a virtual environment, follow these steps:

bash
Copy code
python3 -m venv path/to/venv
source path/to/venv/bin/activate
pip install -r requirements.txt
uvicorn app.main:app --reload
API Endpoints
1. Health Check API
Use the following curl command to check the health of the application:

bash
Copy code
curl --location 'http://0.0.0.0:8000/'
2. Scraping API
Use the following curl command to start scraping. Make sure to provide the appropriate payload and authorization token:

bash
Copy code
curl --location 'http://0.0.0.0:8000/scraper/start' \
  --header 'Authorization: Bearer 1234' \
  --header 'Content-Type: application/json' \
  --data '{
    "pages": 15,
    "url": "https://dentalstall.com/shop/"
  }'
Parameters:
pages: (Optional) The number of pages to scrape.
url: The URL to scrape.
Authorization Header: The Authorization header must contain a valid bearer token (e.g., Bearer 1234).
Configuration (for ease of execution)
The following configuration is currently hardcoded for simplicity:

STATIC_TOKEN = "1234"
PROXY = None
MAX_RETRIES = 3
RETRY_DELAY = 5
You can update these values as per your requirements.