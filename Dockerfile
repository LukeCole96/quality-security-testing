FROM node:18-alpine

WORKDIR /app

RUN apk add --no-cache git && \
    git clone https://github.com/juice-shop/juice-shop.git . && \
    npm install --production

EXPOSE 3000

CMD ["npm", "start"]
