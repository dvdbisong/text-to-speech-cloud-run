# Use the official Python image.
FROM python:3.7

# Copy local code to the container image.
ENV APP_HOME /app
WORKDIR $APP_HOME
COPY . .

# Install production dependencies.
RUN pip install flask gunicorn
RUN pip install flask-wtf
RUN pip install --upgrade google-cloud-texttospeech
RUN pip install flask-bootstrap

# Run the web service on container startup. Here we use the gunicorn
# webserver, with one worker process and 8 threads.
# For environments with multiple CPU cores, increase the number of workers
# to be equal to the cores available.

CMD exec gunicorn --bind :$PORT --workers 1 --threads 8 app:app
#EXPOSE 8000
#CMD ["gunicorn", "-b", "0.0.0.0:8000", "app"]