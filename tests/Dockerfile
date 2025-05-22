FROM python:3.12-alpine

WORKDIR /work/tests

RUN python -m venv /venv && \
    /venv/bin/pip install pytest

COPY . .

# ENV PATH=/venv/bin:$PATH
ENV PYTHONPATH=/work

CMD ["/venv/bin/pytest", "../tests/test_validation_config.py"]
