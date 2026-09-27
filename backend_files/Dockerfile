From python:3.9-slim

WORKDIR /app

COPY . .

RUN pip install --no-cache-dir --upgrade -r requirements.txt

  - '-w 4': Uses 4 worker processes for handling requests
  - 'b 0.0.0.0:7860': Binds the server to port 7860 on all network interfaces
  - 'app:app': Runs the Flask app (assuming 'app.py' contains the Flask instance named 'app')
CMD ["gunicorn", "-w", "4", "-b", "0.0.0.0:7860", "app:learn_api"]
