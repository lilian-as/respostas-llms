FROM python:3.13

WORKDIR /code

COPY . /code/

RUN pip install google-genai
RUN pip install groq

CMD [ "python","app.py" ]