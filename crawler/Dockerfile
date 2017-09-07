# Use an official Python runtime as a parent image
FROM python:3.6

 
WORKDIR /usr/src/crawler
COPY . .
# Install any needed packages specified in requirements.txt
RUN pip install -r requirement.txt


 
CMD ["python3", "bayareanews_crawler.py", "00:50"]