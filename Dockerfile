FROM python:3.8-slim-buster

# --- NETFREE CERT INTSALL ---
ADD https://s1.netfree.link/dl/unix-ca.sh /home/netfree-unix-ca.sh 
RUN cat  /home/netfree-unix-ca.sh | sh
ENV NODE_EXTRA_CA_CERTS=/etc/ca-bundle.crt
ENV REQUESTS_CA_BUNDLE=/etc/ca-bundle.crt
ENV SSL_CERT_FILE=/etc/ca-bundle.crt
# --- END NETFREE CERT INTSALL ---



COPY . /home/app
ARG PORT
ENV PORT=${PORT}
EXPOSE $PORT
ARG user_name=LEA
ENV USER_NAME=${user_name}
RUN useradd -ms /bin/bash $USER_NAME 
USER $USER_NAME
RUN pip install --trusted-host pypi.org --trusted-host files.pythonhosted.org -r /home/app/requirements.txt
WORKDIR /home/app
CMD ["python3","app.py","-h", "0.0.0.0"]