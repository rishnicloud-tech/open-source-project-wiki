# Use a lightweight Nginx image
FROM nginx:alpine

# Copy the built application (dist directory) to the Nginx html directory
COPY dist/ /usr/share/nginx/html/

# Expose port 80
EXPOSE 80

# Start Nginx
CMD ["nginx", "-g", "daemon off;"]
