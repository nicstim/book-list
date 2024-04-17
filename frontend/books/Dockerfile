FROM node:14

WORKDIR /app
COPY package*.json ./

# установить зависимости
RUN npm install
COPY . .
RUN npm run build
EXPOSE 8080

# запустить приложение
CMD [ "npm", "start" ]
