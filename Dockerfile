FROM python:3-alpine
MAINTAINER hsingh23@illinois.edu
RUN pip install twilio requests
ADD site-checker .
ENTRYPOINT python3 monitor_site.py
