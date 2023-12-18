FROM nginxinc/nginx-unprivileged:1-alpine

LABEL maintainer="Robert Treharne"

COPY ./default.config.tpl /etc/nginx/default.config.tpl
COPY ./uwsgi_params /etc/nginx/wsgi_params
COPY ./run.sh /run.sh

ENV LISTEN_PORT=8080
ENV APP_HOST=app
ENV APP_PORT=9090

USER root

RUN mkdir -p /vol/static && \
    chmod -R 755 /vol/static && \
    touch /etc/nginx/conf.d/default.conf && \
    chown nginx:nginx /etc/nginx/conf.d/default.conf && \
    chmod +x /run.sh

VOLUME /vol/static

USER nginx

CMD ["/run.sh"]
