FROM alpine:3.21
RUN apk add --no-cache ffmpeg python3
ENV PYTHONUNBUFFERED=1
COPY 8mb.py /bin/8mb
RUN chmod +x /bin/8mb
ENTRYPOINT ["/bin/8mb"]