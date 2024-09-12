FROM mcr.microsoft.com/playwright:v1.38.0-focal

WORKDIR /app

# Copy the requirements file
COPY requirements.txt .

# Install Python dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy the rest of the application code
COPY . .

# Install Playwright browsers
RUN playwright install chromium

# Set the entry point
ENTRYPOINT ["pytest"]