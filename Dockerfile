FROM python:3.10
ENV PYTHONDONTWRIEBYTECODE 1
ENV PYTHONUNBUFFERED 1
WORKDIR /code
COPY Pipfile Pipfile.lock /code/
RUN pip install pipenv && pipenv install --system
COPY . /code/
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
