FROM java:8
MAINTAINER Stephan Zednik "zednis2@rpi.edu"
ENV REFRESHED_AT 2015-09-28

ENV FUSEKI_BASE /opt/fuseki

# Install wget
RUN \
  apt-get -q update && \
  apt-get -y install wget

RUN mkdir -p ${FUSEKI_BASE}
WORKDIR ${FUSEKI_BASE}

RUN \
  wget --quiet http://www.us.apache.org/dist/jena/binaries/jena-fuseki1-1.3.0-distribution.tar.gz && \
  tar xvzf jena-fuseki1-1.3.0-distribution.tar.gz && \
  cd jena-fuseki1-1.3.0/ && \
  chmod +x fuseki-server s-*

ENV FUSEKI_HOME ${FUSEKI_BASE}/jena-fuseki1-1.3.0
ENV PATH ${FUSEKI_HOME}:${PATH}

# Clean up APT when done.
RUN apt-get clean && rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*

VOLUME ["/etc/fuseki/conf.d", "/var/lib/tdb"]

EXPOSE 3030

WORKDIR $FUSEKI_HOME
ENTRYPOINT ["fuseki-server"]
CMD ["--update", "--loc=/var/lib/tdb", "/ds"]
