FROM nginx
COPY nginx.conf /etc/nginx/nginx.conf
COPY ./dist /usr/share/nginx/html
#COPY host.crt /etc/nginx/
#COPY host.key /etc/nginx/