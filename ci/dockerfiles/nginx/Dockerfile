FROM nginx:1.21-alpine
USER root
WORKDIR /home/django/baseproject
RUN rm /etc/nginx/conf.d/default.conf
COPY nginx.conf /etc/nginx/conf.d
