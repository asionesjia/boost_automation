#
FROM python:3.10.8

#
WORKDIR /boost_automation

#
COPY ./requirements.txt /boost_automation/requirements.txt

#
RUN pip install --no-cache-dir --upgrade -r /boost_automation/requirements.txt

#
COPY ./run.py /boost_automation/run.py

#
COPY ./app /boost_automation/app

#
ENTRYPOINT [ "python" ]

#
CMD [ "./run.py" ]