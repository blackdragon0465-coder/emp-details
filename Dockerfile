#Use official Python image
FROM python:3.12-slim

#Set the working directory 
WORKDIR /app

#Copy all files to the container
COPY . .

#command to run python file
CMD ["python", "emp_details.py"]