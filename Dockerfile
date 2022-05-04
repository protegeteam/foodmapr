FROM python:3.10

WORKDIR /foodmapr

# cache the requirements before the foodmapr install
COPY requirements.txt /foodmapr

RUN pip install --upgrade pip \
    && pip install -r requirements.txt

# download and cache nltk data
RUN mkdir /nltk_data \
    && python -m nltk.downloader -d /nltk_data/ punkt stopwords

ENV USER_NLTK_DATA=/nltk_data

COPY . /foodmapr

RUN pip install .

ENTRYPOINT [ "foodmapr" ]
