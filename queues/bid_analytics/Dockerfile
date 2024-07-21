FROM python
WORKDIR /queues
COPY analytics.py .
RUN pip install pyzmq
CMD ["python", "analytics.py"]