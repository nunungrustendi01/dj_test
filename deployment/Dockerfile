FROM python:3.11

# Set working directory
WORKDIR /usr/src/dj_test_web

# Set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# Install dependencies
RUN apt-get update && apt-get install -y postgresql-client

RUN pip install --upgrade pip
COPY requirements.txt /usr/src/dj_test_web/requirements.txt
RUN pip install -r /usr/src/dj_test_web/requirements.txt

# Copy app
COPY dj_test/ /usr/src/dj_test_web/

# Copy entrypoint
COPY deployment/entrypoint.sh /usr/src/entrypoint.sh
RUN chmod +x /usr/src/entrypoint.sh
ENTRYPOINT ["/usr/src/entrypoint.sh"]