# atlys
##Atlys Assignment

I have created a folder scrapper_app which contain the FastAPI having the required scrapping application <br>


1. The folder contain a docker-compose.yaml file which will help you build the application and run it in docker container<br>
1.1 Make sure you are inside the scrapper_app folder and run the follwoing command
```bash
docker-compose up -d
```
1.2 Once the docker image gets build, it will run the docker container for the application in detched mode, once done, check the docker container is running or not<br>
```bash
docker ps
```

1.3 Once you get the docker image id, check the logs<br>
```bash
docker logs -f <docker-id>
```

1.4 Hit with the Healthcheck API, given below<br>
1.5 Hit the scrapping API with proper payload, given below<br>
1.6 To check the procedure of the scrapping and it got saved in the respective local environment or not exec inside the docker container<br>
```bash
docker exec -it <docker-id> sh
ls
```
    ### you will get list of folders in the root work directory<br>
        - our interest is to check the images inside - downloaded_images
```bash
cd downloaded_images
ls
```
    ### another interest of ours is to check the local storage of scrapped data in json file
        - go back to the root work directory, parent of downloaded_images
        - cat scraped_data.json

## ------- ANOTHER WAYS TO UP AND RUN THE APPLICTION -------

2. The folder contain a Dockerfile which you will use to build and run the application<br>
2.1 Make sure to build the docker image for the application<br>
    - You just need to enter inside the scrapper_app folder and run the following command
```bash
docker build -t app .
```
2.2 Once the image build gets completed then you need to run the image<br>
```bash
docker run -p 8000:8000 app
```

3. If you don't want to run it using Docker then you can user uvicorn -<br>
3.1 You just need to enter inside the scrapper_app folder and install all the dependencies
```bash
pip install -r requirements.txt
```
3.2 And then run the uvicorn command to start the application
```bash
uvicorn app.main:app --reload
```
3.3 If needed do set the environment -
```bash
python3 -m venv path/to/venv
source path/to/venv/bin/activate
pip install -r requirements.txt
uvicorn app.main:app --reload
```

4. There are 2 API's Supported:<br>
4.1 Curl for health check is -
```bash
curl --location 'http://0.0.0.0:8000/'
```
4.2 Curl for scrapping is -
```bash
    curl --location 'http://0.0.0.0:8000/scraper/start' \
        --header 'Authorization: Bearer 1234' \
        --header 'Content-Type: application/json' \
        --data '{
        "pages": 15,
        "url": "https://dentalstall.com/shop/"
        }'
```

The second curl will take pages as optional paramener and the Authorization header in headers.<br>

### for current scenario i have set the following configuration and didn't put it in .env environment file to make the execution easy
```bash
STATIC_TOKEN = "1234"  
PROXY = None 
MAX_RETRIES = 3
RETRY_DELAY = 5
```


