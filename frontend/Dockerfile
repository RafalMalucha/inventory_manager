# Use official Node.js image
FROM node:20-alpine

# Set the working directory inside the container
WORKDIR /app

# Copy package.json and package-lock.json separately for better caching
COPY package*.json ./

# Install dependencies
RUN npm install

# Copy the rest of the application code
COPY . .

RUN npm run build

# Expose port 5173 for Vite's dev server
EXPOSE 5173

CMD ["npm", "run", "dev"]

