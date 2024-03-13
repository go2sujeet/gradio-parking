FROM python:3.12.1

# Set the working directory
WORKDIR /code

# Copy the requirements file
COPY requirements.txt .

# Install the dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy the source code and data
COPY src/ src/
COPY data/ data/

#Expose the port
EXPOSE 8080

# Set the entry point command
CMD ["python", "src/main.py"]