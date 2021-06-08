FROM node:16-alpine
WORKDIR /code
COPY package.json .
COPY package-lock.json .
RUN npm i
COPY . .
